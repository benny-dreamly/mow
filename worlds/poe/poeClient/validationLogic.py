import asyncio
import logging
import traceback

from typing import TYPE_CHECKING

from NetUtils import ClientStatus
from .inputHelper import send_multiple_poe_text

if TYPE_CHECKING:
    from worlds.poe.Client import PathOfExileContext
    from worlds.poe import PathOfExileWorld
from . import itemFilter
from . import gggAPI
from . import fileHelper
from . import inputHelper
from . import tts
from . import textUpdate

import worlds.poe.Items as Items
import worlds.poe.Locations as Locations

import worlds.poe.Options as Options

is_char_in_logic = True

_debug = True
_verbose_debug = False

logger = logging.getLogger("poeClient.validationLogic")
logger.setLevel(logging.DEBUG)

PASSIVE_POINT_ITEM_ID = Items.get_by_name("Progressive passive point")["id"]

last_zone = None
# Timeouts (seconds)
TIMEOUT = 5.0
async def when_enter_new_zone(ctx: "PathOfExileContext", line: str):
    global last_zone, is_char_in_logic
    zone = textUpdate.get_zone_from_line(ctx, line)
    last_zone = zone
    if not zone:
        return
    
    
    char = None
    found_items_list: list[Locations.LocationDict] = []
    if ctx.character_name is None or ctx.character_name == "":
        logger.info("Character name is not set, cannot validate.")
        await asyncio.wait_for(send_multiple_poe_text(["/itemfilter __invalid", "Character name is not set, cannot validate."]), TIMEOUT)
        return
    try:
        char = (await asyncio.wait_for(gggAPI.get_character(ctx.character_name),TIMEOUT)).character
        ctx.last_response_from_api.setdefault("character", {})[ctx.character_name] = char
        ctx.last_character_level = char.level
        found_items_list = get_found_base_item_locations(char)
    except Exception as e:
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(f"Error fetching character {ctx.character_name}: {e}\nTraceback:\n{tb_str}")
        raise

    logic_errors = await validate_and_update(ctx, char, found_items_list)
    victory_task = check_for_victory(ctx, zone, char)

    # THIS IS FOR DEBUGGING PURPOSES, I'm tired of respeccing my character to test the logic, lol
    if False:
        is_char_in_logic = True

    if not is_char_in_logic:
        error_msg = ", and ".join(logic_errors) if logic_errors else "unknown errors"
        await asyncio.wait_for(send_multiple_poe_text(["/itemfilter __invalid", f"@{ctx.character_name} you are out of logic: {error_msg}"]), TIMEOUT)
    elif victory_task:
        pass # callback handles victory and chat sending
    else:
        await asyncio.wait_for(inputHelper.important_send_poe_text("/itemfilter __ap", retry_times=40, retry_delay=0.5), TIMEOUT)

def check_for_victory(ctx: "PathOfExileContext", zone: str, char: gggAPI.Character) -> asyncio.Task | None:
    goal = ctx.game_options.get("goal", -1)
    return_task: asyncio.Task | None = None
    if goal == -1:
        logger.info("ERROR: No goal set in client options.")
        raise ValueError("No goal set in client options.")

    def send_goal():
        asyncio.create_task(ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))
        asyncio.create_task(inputHelper.important_send_poe_text("Congratulations! You have won!", retry_times=40, retry_delay=0.5))
        ctx.finished_game = True
        ctx.victory = True
    

    if \
    (goal == Options.Goal.option_complete_act_1 and zone == "The Southern Forest") or \
    (goal == Options.Goal.option_complete_act_2 and zone == "The City of Sarn") or \
    (goal == Options.Goal.option_complete_act_3 and zone == "The Aqueduct") or \
    (goal == Options.Goal.option_complete_act_4 and zone == "The Slave Pens") or \
    (goal == Options.Goal.option_kauri_fortress_act_6 and zone == "The Karui Fortress") or \
    (goal == Options.Goal.option_complete_act_6 and zone == "The Bridge Encampment") or \
    (goal == Options.Goal.option_complete_act_7 and zone == "The Sarn Ramparts") or \
    (goal == Options.Goal.option_complete_act_8 and zone == "The Blood Aqueduct") or \
    (goal == Options.Goal.option_complete_act_9 and zone == "Oriath Docks") or \
    (goal == Options.Goal.option_complete_the_campaign and zone == "Karui Shores"):
        return asyncio.create_task(textUpdate.callback_if_valid_char(ctx, send_goal))


    async def send_boss_update_text(boss_set: set[int]):
        #ids of bosses defeated
        boss_names = ""
        bosses = []
        for i in boss_set:
            bosses.append(Locations.bosses_by_id[i].get("name", "Unknown Boss"))
        if bosses:
            await asyncio.create_task(inputHelper.send_poe_text(f"@{ctx.character_name} You have defeated {", ".join(bosses)}!", retry_times=40, retry_delay=0.5))
    # we should probably create a location and fill it with a goal item for each boss.
    if goal == Options.Goal.option_defeat_bosses:
        held_items = get_held_item_names_ilvls_from_char(char)
        boss_sent = []
        bosses_for_goal = ctx.game_options.get("bosses_for_goal", [])
        for boss in bosses_for_goal:
            boss_data = Locations.bosses.get(boss)
            if not boss_data:
                logger.error(f"Boss {boss} not found in Locations.bosses.")
                raise ValueError(f"Boss {boss} not found in Locations.bosses.")
            drops = boss_data.get("drops", [])
            for item, ilvl in held_items:
                if item in [i["name"] for i in drops]:
                    if ilvl and drops[item].get("ilvl", 0) and ilvl < drops[item]["ilvl"]:
                        continue # item is not high enough level
                    logger.info(f"Found goal item {item} in {zone}.")
                    boss_sent.append(boss)
                    return_task = (asyncio.create_task(ctx.check_locations({boss_data['id']}))
                            .add_done_callback(lambda x: asyncio.create_task(
                        send_boss_update_text(x.result()))))

        received_item_names = {Locations.bosses_by_id[i].get("name","") for i in {j.item for j in ctx.items_received} if i in Locations.bosses_by_id} | {f"defeat {boss}" for boss in boss_sent}
        required_completion_items = {f"defeat {boss}" for boss in bosses_for_goal}
        
        # Check if we have ALL required boss completion items
        if required_completion_items.issubset(received_item_names):
            logger.info(f"Victory condition met! All bosses defeated: {bosses_for_goal}")
            return asyncio.create_task(textUpdate.callback_if_valid_char(ctx, send_goal))
        else:
            missing = required_completion_items - received_item_names
            logger.debug(f"Still missing boss completions: {missing}")
    
    return return_task


async def validate_and_update(ctx: "PathOfExileContext", char, found_items_list: list[Locations.LocationDict]) -> list[str]:
    global is_char_in_logic
    validate_errors = []
    if ctx is None:
        # something is wrong, are we not connected?
        logger.info("Context is None, cannot validate character.")
        validate_errors.append("Context is None, cannot validate character.")
        return validate_errors
    character_name = ctx.character_name
    if character_name is None or character_name == "":
        logger.info("Character name is not set, cannot validate.")
        validate_errors.append("Character name is not set, cannot validate.")
        return validate_errors
    # defenseive programming end.

    total_received_items = [
        item for network_item in ctx.items_received
        if (item := Items.item_table.get(network_item.item)) is not None
    ]
    validate_errors = validate_char_equipment(char, ctx, total_received_items)

    location_ids_to_check = set()
    #add items to locations_to_check
    for location_dict in found_items_list:
        logger.debug(f"Found item: {location_dict["name"]}")
        location_id = location_dict["id"]
        if location_id is not None:
            location_ids_to_check.add(location_id)
    
    #add levels to locations_to_check
    if ctx.game_options.get("add_leveling_up_to_location_pool", True):
        for level in range(2, ctx.last_character_level + 1):
            if _verbose_debug: logger.debug(f"[DEBUG] Adding level {level} to locations to check.")
            level_location_name = Locations.get_lvl_location_name_from_lvl(level)
            location_id = Locations.id_by_level_location_name.get(level_location_name)
            if location_id is not None:
                location_ids_to_check.add(location_id)

    location_ids_to_check = location_ids_to_check & ctx.missing_locations
    passives = 0
    for id in location_ids_to_check:
        network_item = ctx.locations_info[id]
        if network_item.item == PASSIVE_POINT_ITEM_ID and network_item.player == ctx.slot:
            passives += 1


    validate_errors.extend(validate_passive_points(char, ctx, total_received_items, passives))
    is_char_in_logic = True if len(validate_errors) == 0 else False

    if len(location_ids_to_check) > 0:
        logger.debug(f"[DEBUG] Locations to check: {location_ids_to_check}")
        location_ids_to_check = await ctx.check_locations(location_ids_to_check)
    else:
        logger.debug("[DEBUG] No locations to check, skipping check_locations.")

    if not is_char_in_logic:
        await update_filter_to_invalid_char_filter(errors=validate_errors, enable_tts=ctx.tts_options.enable, tts_speed=ctx.tts_options.speed)
    else:
        itemFilter.update_item_filter_from_context(ctx, recently_checked_locations=location_ids_to_check)
    return validate_errors


def validate_passive_points(character: gggAPI.Character,  ctx: "PathOfExileContext", total_received_items: list[Items.ItemDict], points_from_this_zone: int = 0) -> list[str]:
    """
    Validate the passive points of the character.
    This function checks if the character has the correct number of passive points based on their level.
    """
    errors = []
    if ctx.game_options.get("passivePointsAsItems", True):
        passive_points = len([i["name"] for i in total_received_items if i["name"] == 'Progressive passive point'])
        passive_points += points_from_this_zone
        passives_used = len(character.passives.hashes)  # number of passives allocated -- this includes the ascendency points
        ctx.passives_available = passive_points
        ctx.passives_used = passives_used
        if passives_used > passive_points:
            errors.append(f"{passives_used - passive_points} Over-allocated passive points")
    return errors

def validate_char_equipment(character: gggAPI.Character, ctx: "PathOfExileContext", total_received_items: list[Items.ItemDict]) -> list[str]:
    # Perform validation logic here

    if character is None:
        return ["Character name is not set, cannot validate."]

    errors = list()

    if not total_received_items:
        logger.error("No valid items found in total_received_items. Are you sure the item table is correct?")
        return ["No items received from the server... are you sure you are connected?"]

    simple_equipment_slots = ["BodyArmour","Amulet","Belt","Boots","Gloves","Helmet"]

    normal_flask_count = 0
    magic_flask_count = 0
    unique_flask_count = 0

    # --------- VALIDATION LOGIC STARTS HERE ---------

    if character.class_ not in [i["name"] for i in total_received_items]:
        errors.append(f"Class {character.class_}")

    gucci_rarity_check = {}
    for equipped_item in character.equipment:
        rarity = equipped_item.rarity
        gucci_rarity_check.setdefault(rarity, 0)
        gucci_rarity_check[rarity] += 1
        # simple checks.
        for slot in simple_equipment_slots:
            if equipped_item.inventoryId == slot:
                errors.append(rarity_check(total_received_items, rarity, slot))
                
        if equipped_item.inventoryId == "Ring":
            errors.append(rarity_check(total_received_items, rarity, "Ring (left)"))
        if equipped_item.inventoryId == "Ring2":
            errors.append(rarity_check(total_received_items, rarity, "Ring (right)"))
 #       if equipped_item.inventoryId == "Offhand":
 #           if equipped_item.baseType in Items.quiver_base_types:
 #               errors.append(rarity_check(total_received_items, rarity, "Quiver"))
 #           else:
 #               errors.append(rarity_check(total_received_items, rarity, "Shield"))
        if equipped_item.inventoryId == "Weapon" or equipped_item.inventoryId == "Offhand":
            for prop in equipped_item.properties:
                prop_name = prop.name
                for weapon_base_type in Items.held_equipment_types:
                    if prop_name.lower().endswith(weapon_base_type.lower()):
                        errors.append(rarity_check(total_received_items, rarity, weapon_base_type))

        equipped_sockets = 0
        if equipped_item.socketedItems is not None:
            for socketed_item in equipped_item.socketedItems:
                if socketed_item.support:
                    equipped_sockets += 1
                if (socketed_item.baseType not in [i["name"] for i in total_received_items] and
                        "eye jewel" not in socketed_item.baseType.lower()): # eye jewels are not tracked right now.
                    errors.append(f"Socketed {socketed_item.baseType} in {equipped_item.inventoryId}")

        links = [i["name"] for i in total_received_items if i["name"] == f"Progressive max links - {equipped_item.inventoryId}"]
        if len(links) < equipped_sockets:
            errors.append(f"Too many links for {equipped_item.baseType}")

        if equipped_item.inventoryId == "Flask":
            flask_rarity = equipped_item.rarity
            if flask_rarity == "Normal":
                normal_flask_count += 1
            elif flask_rarity == "Magic":
                magic_flask_count += 1
            elif flask_rarity == "Unique":
                unique_flask_count += 1
                
    # get count of items.name that match the progressive unlocks
    if normal_flask_count > len([i["name"] for i in total_received_items if i["name"] == 'Progressive Normal Flask Unlock']):
        errors.append("Normal Flasks")
    if magic_flask_count > len([i["name"] for i in total_received_items if i["name"] == 'Progressive Magic Flask Unlock']):
        errors.append("Magic Flasks")
    if unique_flask_count > len([i["name"] for i in total_received_items if i["name"] == 'Progressive Unique Flask Unlock']):
        errors.append("Unique Flasks")

    gucci_hobo_mode = ctx.game_options.get("gucciHobo", False)
    if gucci_hobo_mode == 1 or gucci_hobo_mode == 2 or gucci_hobo_mode ==3:
        normal_gear = gucci_rarity_check.setdefault("Normal", 0)
        magic_gear = gucci_rarity_check.setdefault("Magic", 0)
        rare_gear = gucci_rarity_check.setdefault("Rare", 0)
        if gucci_hobo_mode == Options.GucciHoboMode.option_allow_one_slot_of_any_rarity and  normal_gear + magic_gear + rare_gear > 1: #options_allow_one_slot_of_any_rarity
            errors.append("Gucci Hobo Mode - Only one item allowed of any rarity")
        if gucci_hobo_mode == Options.GucciHoboMode.option_allow_one_slot_of_normal_rarity and (normal_gear > 1 or magic_gear + rare_gear > 0):  # options_allow_one_slot_of_normal_rarity
            errors.append("Gucci Hobo Mode - Only one normal item allowed")
        if gucci_hobo_mode == Options.GucciHoboMode.option_no_non_unique_items and (normal_gear + magic_gear + rare_gear > 0): # option_no_non_unique_items
            errors.append("Gucci Hobo Mode - No non-unique items allowed")

    errors = [x for x in errors if x]  # filter out empty strings
    if _debug and errors:
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
        logger.info("YOU ARE OUT OF LOGIC: " + ", ".join(errors))
    return errors
    

def rarity_check(total_recieved_items, rarity: str, equipmentId: str) -> str | None:
    valid = True
    if rarity == "Unique":
        valid = True if f"Unique {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    elif rarity == "Rare":
        valid = True if f"Rare {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    elif rarity == "Magic":
        valid = True if f"Magic {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    else:
        valid = True if f"Normal {equipmentId}" in [i["name"] for i in total_recieved_items] else False
    
    if not valid:
        return equipmentId
    else: 
        return None


#async def update_filter(ctx: "PathOfExileContext") -> bool:
#    item_filter_string = ""
#    missing_location_ids = ctx.missing_locations
#    for base_item_location_id in missing_location_ids:
#
##        item_text = Items.get(base_item_location_id, "Unknown Item") # this needs to be the scouted item name, unless the options specify otherwise
#        network_item = ctx.locations_info[base_item_location_id]
#        item_text = tts.get_item_name_tts_text(ctx, network_item)
#        filename =  f"{item_text.lower()}_{tts.WPM}.wav"
#        base_item_location_name = ctx.location_names.lookup_in_game(base_item_location_id)
#        item_filter_string += itemFilter.generate_item_filter_block(base_item_location_name, f"{itemFilter.filter_sounds_dir_name}/{fileHelper.safe_filename(filename)}")+ "\n\n"
#
#    if item_filter_string:
#        itemFilter.write_item_filter(item_filter_string)
#        logger.info(f"Item filter updated with {len(missing_location_ids)} items.")
#    return True

async def update_filter_to_invalid_char_filter(errors: list[str], enable_tts: bool = True, tts_speed: int = 250) -> None:

    if enable_tts:
        if len(errors) > 1:
            error_text = " and ... ".join(errors)
        else:
            error_text = errors[0]
        filename = f"{fileHelper.short_hash(error_text)}_{tts.WPM}.wav" # this could be a long text, so we use a hash
        full_error_text = f"YOU ARE OUT OF LOGIC: {error_text}"
        await tts.safe_tts_async(
            text=full_error_text,
            filename=itemFilter.filter_sounds_path / f"{filename}",
            rate=tts_speed
        )
        invalid_item_filter_string = itemFilter.generate_invalid_item_filter_block(f"{itemFilter.filter_sounds_dir_name}/{filename}")
        itemFilter.write_item_filter(item_filter=invalid_item_filter_string, item_filter_import=None, file_path=itemFilter.invalid_filter_file_path)
    else:
        invalid_item_filter_string = itemFilter.generate_invalid_item_filter_block_without_sound()
        itemFilter.write_item_filter(item_filter=invalid_item_filter_string, item_filter_import=None, file_path=itemFilter.invalid_filter_file_path)

def get_held_item_names_ilvls_from_char(char: gggAPI.Character) -> list[tuple[str, int]]:
    """
    Returns a list of all items from the character's inventory and equipment.
    """
    all_items: list[tuple[str, int]] = []
    full_found_list = char.inventory #+ char.equipment #check only non-equipped items
    for item in full_found_list:
        all_items.append((item.name if item.name else item.baseType, item.ilvl))  # Item is a dataclass, not a dict

    return all_items

def get_found_base_item_locations(char: gggAPI.Character) -> list[Locations.LocationDict]:
    found_items: list[Locations.LocationDict] = []
    try:
        full_found_list = char.inventory + char.equipment
        for item in full_found_list:
            if item.baseType in Locations.base_item_locations_by_base_item_name:
                found_items.append(
                    Locations.base_item_locations_by_base_item_name[item.baseType]
                )
                logger.debug(f"[DEBUG] Item in inventory: {item.baseType}")
    except Exception as e:
        logger.error(f"Error fetching found items: {e}")
        raise e
    return found_items
