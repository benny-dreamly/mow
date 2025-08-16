import argparse
import os
import multiprocessing
import logging
import typing
import ModuleUpdate

ModuleUpdate.requirements_files.add(os.path.join("WebHostLib", "requirements.txt"))
ModuleUpdate.update()

# in case app gets imported by something like gunicorn
import Utils
import settings

if typing.TYPE_CHECKING:
    from flask import Flask

Utils.local_path.cached_path = os.path.dirname(__file__)
settings.no_gui = True
configpath = os.path.abspath("config.yaml")
if not os.path.exists(configpath):  # fall back to config.yaml in home
    configpath = os.path.abspath(Utils.user_path('config.yaml'))


def get_app() -> "Flask":
    from WebHostLib import register, cache, app as raw_app
    from WebHostLib.models import db

    app = raw_app
    if os.path.exists(configpath) and not app.config["TESTING"]:
        import yaml
        app.config.from_file(configpath, yaml.safe_load)
        logging.info(f"Updated config from {configpath}")
    # inside get_app() so it's usable in systems like gunicorn, which do not run WebHost.py, but import it.
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--config_override', default=None,
                        help="Path to yaml config file that overrules config.yaml.")
    args = parser.parse_known_args()[0]
    if args.config_override:
        import yaml
        app.config.from_file(os.path.abspath(args.config_override), yaml.safe_load)
        logging.info(f"Updated config from {args.config_override}")
    if not app.config["HOST_ADDRESS"]:
        logging.info("Getting public IP, as HOST_ADDRESS is empty.")
        app.config["HOST_ADDRESS"] = Utils.get_public_ipv4()
        logging.info(f"HOST_ADDRESS was set to {app.config['HOST_ADDRESS']}")

    register()
    cache.init_app(app)
    db.bind(**app.config["PONY"])
    db.generate_mapping(create_tables=True)
    return app


def copy_tutorials_files_to_static(app=None) -> None:
    import shutil
    import zipfile
    from werkzeug.utils import secure_filename

    zfile: zipfile.ZipInfo

    from worlds.AutoWorld import AutoWorldRegister
    worlds = {}
    for game, world in AutoWorldRegister.world_types.items():
        if hasattr(world.web, 'tutorials') and (not world.hidden or game == 'Archipelago'):
            worlds[game] = world

    base_target_path = Utils.local_path("WebHostLib", "static", "generated", "docs")
    shutil.rmtree(base_target_path, ignore_errors=True)
    for game, world in worlds.items():
        # copy files from world's docs folder to the generated folder
        target_path = os.path.join(base_target_path, secure_filename(game))
        os.makedirs(target_path, exist_ok=True)

        if world.zip_path:
            zipfile_path = world.zip_path

            assert os.path.isfile(zipfile_path), f"{zipfile_path} is not a valid file(path)."
            assert zipfile.is_zipfile(zipfile_path), f"{zipfile_path} is not a valid zipfile."

            with zipfile.ZipFile(zipfile_path) as zf:
                for zfile in zf.infolist():
                    if not zfile.is_dir() and "/docs/" in zfile.filename:
                        zfile.filename = os.path.basename(zfile.filename)
                        with open(os.path.join(target_path, secure_filename(zfile.filename)), "wb") as f:
                            f.write(zf.read(zfile))
        else:
            world_dir = os.path.dirname(world.__file__)
            source_path = None
            
            root_docs_path = Utils.local_path(world_dir, "docs")
            if os.path.exists(root_docs_path) and os.path.isdir(root_docs_path):
                source_path = root_docs_path
            else:
                source_path = find_docs_folder_recursive(world_dir)
            
            if source_path:
                try:
                    files = os.listdir(source_path)
                    for file in files:
                        file_path = Utils.local_path(source_path, file)
                        if os.path.isfile(file_path):
                            shutil.copyfile(file_path,
                                            Utils.local_path(target_path, secure_filename(file)))
                except (OSError, IOError) as e:
                    logging.warning(f"Failed to copy docs for {game}: {e}")
            else:
                logging.info(f"No docs folder found for {game}")


def find_docs_folder_recursive(root_dir, max_depth=3):
    """
    Recursively search for a "docs" folder in subdirectories.
    Returns  Path to docs folder if found, None otherwise
    """
    def search_recursive(current_dir, current_depth):
        if current_depth > max_depth:
            return None
        
        try:
            for item in os.listdir(current_dir):
                item_path = os.path.join(current_dir, item)
                if os.path.isdir(item_path):
                    if item == "docs":
                        return item_path
                    # Recursively search subdirectories
                    result = search_recursive(item_path, current_depth + 1)
                    if result:
                        return result
        except (OSError, PermissionError):
            pass
        
        return None
    
    return search_recursive(root_dir, 0)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)


    from WebHostLib.autolauncher import autohost, autogen, stop
    from WebHostLib.options import create as create_options_files

    try:
        from WebHostLib.lttpsprites import update_sprites_lttp
        update_sprites_lttp()
    except Exception as e:
        logging.warning("Could not update LttP sprites: %s", e)
    app = get_app()
    create_options_files()
    copy_tutorials_files_to_static(app)
    if app.config["SELFLAUNCH"]:
        autohost(app.config)
    if app.config["SELFGEN"]:
        autogen(app.config)
    if app.config["SELFHOST"]:  # using WSGI, you just want to run get_app()
        if app.config["DEBUG"]:
            app.run(debug=True, port=app.config["PORT"])
        else:
            from waitress import serve
            serve(app, port=app.config["PORT"], threads=app.config["WAITRESS_THREADS"])
    else:
        from time import sleep
        try:
            while True:
                sleep(1)  # wait for process to be killed
        except (SystemExit, KeyboardInterrupt):
            pass
    stop()  # stop worker threads
