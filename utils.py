import json
from ansi import Ansi
from logger import Logger
import tomllib

with open("configuration.toml", "rb") as f:
    toml_data = tomllib.load(f)

menu_elems = toml_data.get("menu")
json_config = toml_data.get("json")

# HELP: posible unbound variable here aswell

class Utils:

    # Loading toml config or fallback default with return:

    @staticmethod
    def json_file_name():
        json_file_name = json_config.get("json_file_name")
        if json_file_name:
            return json_file_name
        else:
            return "alarms.json"


    @staticmethod
    def welcome_message():
        welcome_message = menu_elems.get("welcome_message")
        if welcome_message:
            return welcome_message
        else:
            return "Hello and welcome choose an optioN:"

    @staticmethod
    def pointer():
        config_pointer = menu_elems.get("pointer")
        if config_pointer:
            return config_pointer
        else: # toml return None if no value is specified so default to this:
            return ">"

    # End loading toml file

    @staticmethod
    def alarms_options():
        options = ["CPU", "MEMORY", "DISK", "save", "return"]
        message = "Create an alarm for:"
        print(message)
        for num, item in enumerate(options, 1):
            menu_print = f"{Utils.pointer()} {Ansi.RED} {num} {Ansi.END} {item}"
            print(menu_print)
            # print(Utils.pointer(), {Ansi.RED, num, Ansi.END}, str(item))

    @staticmethod
    def read_alarms_json():
        try:
            with open(Utils.json_file_name(), mode="r", encoding="utf-8") as f:
                # TODO: can you save and load json with integer values or are
                # json files always str?
                # How to make the json data integers the alarm_levels.
                # WARNING: ERROR LOADING AN EMPTY JSON FILE?
                try:
                    data = json.load(f)
                    print("Loading previously configured alarms...")
                    return data
                except json.JSONDecodeError:
                    print("Json error, resorting to an empty dictionary.")
                    return {}
        except FileNotFoundError:
            print("No json alarm file found, creating a new json alarm file.")
            with open(Utils.json_file_name(), mode="w", encoding="utf-8") as f:
                empty_json_data = {}
                json.dump(empty_json_data, f, indent = 4)
            Logger.logger_file_not_found(Utils.json_file_name())

    # Merge with the other save_alarm_json make it take a data parameter like
    # this: def save_alarm_json(data): so I can reduce the amount of methods
    # from two to one the read_alarms_json could be merged somehow?
    @staticmethod
    def save_alarm_json():
        try:
            with open(Utils.json_file_name(), mode="w", encoding="utf-8") as f:
                json.dump(Delete_alarm.data, f)
        except FileNotFoundError:
            pass
