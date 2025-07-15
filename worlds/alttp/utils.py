def get_shuffle_ganon(world, player):
    """Helper function to get shuffle_ganon value regardless of whether world is MultiWorld or ALTTPWorld."""
    # If world has 'worlds' attribute, it's MultiWorld, else it's per-player World
    if hasattr(world, "worlds") and hasattr(world.worlds, "__getitem__"):
        return world.worlds[player].shuffle_ganon
    # Otherwise, assume it's a per-player world instance
    return world.shuffle_ganon 