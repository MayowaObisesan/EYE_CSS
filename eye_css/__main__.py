import os
import yaml


class Eye:
    eye_css_config_data = dict()
    eye_start_valid = False

    import argparse
    parser = argparse.ArgumentParser(description="Eye CSS - A Dynamic CSS Utility-first library written in python.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="help", help="A Dynamic CSS Utility-first library. Just run this file with a configuration file, or define where to save the css for you. Also gives you a CSS cheatsheet for your projects, no need to memorize the css definitions.")
    group.add_argument("-q", "--quiet", action="help", help="A Dynamic CSS Utility-first library written in python.")

    parser.add_argument("file", nargs="?", default="", type=str, help="Eye.css config file")
    args = parser.parse_args()

    if bool(args.file):
        try:
            if os.path.isfile(args.file):
                EYE_CONFIG_FILE = args.file
                with open(args.file, "r") as eye_config_file:
                    eye_css_config_data = yaml.safe_load(eye_config_file)
                    eye_config_file.close()
            elif os.path.isdir(args.file):
                raise FileNotFoundError
            else:
                raise Exception
        except NameError as err:
            print(f"Expected eye_config.yml, got {os.path.basename(args.file)}")
        except FileNotFoundError as err:
            print("Oops. You specified a directory instead.")
        except Exception as err:
            print("Cannot Start Eye.css. Check your config file.")
        else:
            # if eye_css_config_data.get("eye") is not None:
            if eye_config := eye_css_config_data.get("eye"):
                # we do not make provision for multiple directories to be watched because the watcher library being used
                # does not support multiple directories being watched. - August 25, 2022.
                # There are alternatives to the watcher library but not using the alternatives yet. - September 4, 2022.
                DIRECTORY_TO_WATCH = eye_css_config_data.get("eye").get("input_directory", "")
                if not os.path.isabs(DIRECTORY_TO_WATCH):
                    watched_directory_path = os.path.dirname(args.file)
                    DIRECTORY_TO_WATCH = os.path.realpath(os.path.join(watched_directory_path, DIRECTORY_TO_WATCH))
                EXTENSIONS_TO_WATCH = eye_css_config_data.get("eye").get("input_extensions", "").split(",")

                OUTPUT_PATH = eye_css_config_data.get("eye").get("output_path", "") or os.path.dirname(args.file)
                OUTPUT_NAME = eye_css_config_data.get("eye").get("output_name", "")
                EYE_CSS_OUTPUT = os.path.join(OUTPUT_PATH, OUTPUT_NAME)

                EXACT_FILE = eye_css_config_data.get("eye").get("input_exact_files", "")

                EXCLUDE_DIRECTORY = eye_css_config_data.get("eye").get("exclude_directory", "")
                EXCLUDE_FILES = eye_css_config_data.get("eye").get("exclude_files", "")

                # ======================== #
                # SCROLLBAR CONFIGURATIONS - MARCH 26, 2023.
                # ======================== #
                SCROLLBAR_COLOR = eye_config.get("scrollbar_color", "#EEEEEE")
                SCROLLBAR_COLOR_DARK = eye_config.get("scrollbar_color_dark", "#222222")
                SCROLLBAR_WIDTH = eye_config.get("scrollbar_width", "8px")
                SCROLLBAR_WIDTH_SMALL = eye_config.get("scrollbar_width_small", "4px")
                SCROLLBAR_HEIGHT = eye_config.get("scrollbar_height", "8px")
                SCROLLBAR_HEIGHT_SMALL = eye_config.get("scrollbar_height_small", "1px")

                SCROLLBAR_TRACK_COLOR = eye_config.get("scrollbar_track_color", "#F3F3F3")
                SCROLLBAR_TRACK_COLOR_DARK = eye_config.get("scrollbar_track_color_dark", "#222222")
                SCROLLBAR_TRACK_RADIUS = eye_config.get("scrollbar_track_radius", "0px")

                SCROLLBAR_THUMB_COLOR = eye_config.get("scrollbar_thumb_color", "#D7D7D7")
                SCROLLBAR_THUMB_COLOR_DARK = eye_config.get("scrollbar_thumb_color_dark", "#444444")
                SCROLLBAR_THUMB_RADIUS = eye_config.get("scrollbar_thumb_radius", "0px")
            else:
                DIRECTORY_TO_WATCH = eye_css_config_data.get("input_directory", "")
                EXTENSIONS_TO_WATCH = eye_css_config_data.get("input_extensions", "")
                EYE_CSS_OUTPUT = eye_css_config_data.get("output_name", "")

            assert len(eye_css_config_data.keys()) > 0, "Error processing eye_css config File. Check the file once more."
            eye_start_valid = True
    else:
        print("You need to specify an eye_config.yml file")

    def start(self):
        if self.eye_start_valid:
            from eye_css.eye_watcher import EyeWatcher
            EyeWatcher().run()
        # else:
        #     return "You need to specify an eye_config.yml file"


if __name__ == "__main__":
    Eye().start()
