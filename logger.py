import os.path
from datetime import datetime
import tomllib

# TODO: create configuration.toml if it dosn't exist with default values
with open("configuration.toml", "rb") as f:
    # TypeError: File must be opened in binary mod e, e.g. use `open('foo.toml', 'rb')`
    toml_data = tomllib.load(f)

logger_elems = toml_data.get("logger")
# log icons (require https://github.com/ryanoasis/nerd-fonts):

class Logger():

    '''Logger class with configuration'''

    log_spacing = " --- "

    if logger_elems.get("log_spacing"):
        log_spacing = logger_elems.get("log_spacing")
    else:
        log_spacing = " --- " # default icon

    # TOML_CONFIGURATION

    # ICONS
    # TODO: make this into a config class OOP for less verbose structure:
    #
    if logger_elems.get("folder_icon"):
        folder_icon = logger_elems.get("folder_icon")
    else:
        folder_icon = "📁" # default icon

    if logger_elems.get("alarm_icon"):
        alarm_icon = logger_elems.get("alarm_icon")
    else:
        alarm_icon = "󰀡" # default icon

    if logger_elems.get("json_icon"):
        json_icon = logger_elems.get("json_icon")
    else:
        json_icon = "" # default icon

    if logger_elems.get("initalize_icon"):
        initalize_icon = logger_elems.get("initalize_icon")
    else:
        json_icon = "" # default icon

    if logger_elems.get("date_format"):
        date_format = logger_elems.get("date_format")
    else:
        date_format = "%d/%m/%Y %H:%M:%S"

    if logger_elems.get("log_save_path"):
        log_save_path = logger_elems.get("log_save_path")
    else:
        log_save_path = "./"

    if logger_elems.get("log_name"):
        log_name = logger_elems.get("log_name")
    else:
        log_name = "log.txt"

    # HARDCODED
    # folder_icon = "📁"
    # alarm_icon = "󰀡"
    # json_icon = ""
    # initalize_icon = ""

    # DATE
    # date_format = "%d/%m/%Y %H:%M:%S"
    # TODO: Can you merge these two into a oneliner?
    now = datetime.now()
    date_time = now.strftime(date_format)
    # log_save_path = "./" # REVIEW: need to be able to handle ""?.
    # log_name = "log.txt"
    log_full_save = log_save_path + log_name

    @staticmethod
    # REVIEW: WIP no support for log_save_path = "" handeling
    # Check if path exist or not else create it.
    def logger_path():
        # try catch here instead
        isExist = os.path.exists(Logger.log_save_path)
        if isExist is None:
            # ERROR handling for none correctly formated path
            print("error this is no path name")
        elif not isExist:
            os.makedirs(Logger.log_save_path)
            print("The new directory is created!")
            # TODO: create a log entry again for the folder created
            # Make filepath a new method

    @staticmethod
    # creates the logger or loggit as loaded at startup.
    def logger():
        Logger.logger_path()
        try:
            check_file = os.path.isfile(Logger.log_full_save)
            if not check_file:
                Logger.logger_write(f"{Logger.initalize_icon} log file created.", mode="w", newline="")
                print(f"log file created at {Logger.date_time}")
            if check_file:
                Logger.logger_write(f"{Logger.initalize_icon} logger loaded.")
                print("logger loaded")
        # except Exception:
        except FileNotFoundError:
            print("error no file!")

    @staticmethod
    def logger_write(write_string, mode="a", newline="\n"): # default set to append optional param set to append
        with open(Logger.log_full_save, mode=f"{mode}", encoding="utf-8") as f:
            f.write(f"{newline}")
            f.write(Logger.date_time)
            f.write(Logger.log_spacing)
            f.write(write_string)

    # TODO: make it absolute path instead
    @staticmethod
    def logger_file_not_found(file_name):
        Logger.logger_write(f"{Logger.folder_icon} File {file_name} not found.")

    @staticmethod
    def logger_save_alarm_reached(alarm, value):
        Logger.logger_write(f"{Logger.alarm_icon} Alarm {alarm} with value {value} has been reached.")

    @staticmethod
    def logger_json_file_created(file_name):
        Logger.logger_write(f"{Logger.json_icon} Json file with name: {file_name} has been created.")

    # tester method:
    @staticmethod
    def test_logger():
        Logger.logger()
        Logger.logger_file_not_found("test.json")
        Logger.logger_save_alarm_reached("CPU TEST", "50")
        Logger.logger_json_file_created("test.json")

Logger.test_logger()
