import psutil
from utils import Utils
from logger import Logger
from sys import platform
import subprocess

json_data = Utils.read_alarms_json()

class Monitor():
    monitor = False

    disk = psutil.disk_usage("/")
    memory = psutil.virtual_memory()

    ram_used_gb = round(memory.used / (1024 ** 3),1)
    ram_total_gb = round(memory.total / (1024 ** 3))
    disk_used_gb = round(disk.used / (1024 ** 3))
    disk_total_gb = round(disk.total / (1024 ** 3))

    @staticmethod
    def start_monitor():
        if Monitor.monitor:
            print("monitor already started")
        else:
            print("monitor started")
            Monitor.monitor = True
            Logger.logger_write("Monitor started")

    @staticmethod
    def MEMORY():
        return psutil.virtual_memory()[2]

    @staticmethod
    def DISK():
        return psutil.disk_usage('/')[3]

    @staticmethod
    def CPU():
        return psutil.cpu_percent(interval=1)


    @staticmethod
    def run_command(cmd):
        try:
            result = subprocess.Popen(cmd)
            return result.stdout
        except Exception as error:
            return f"There was an error: {error}"

    @staticmethod
    def monitor_mode():
        json_data = Utils.read_alarms_json()
        if bool(json_data) is False:
            print("please add alarms first")
        else:
            print("Monitor mode started, press C-c to exit")
            while True:
                try:
                    for x in json_data["CPU"]:
                        if Monitor.CPU() >= int(x):
                            print(f"ALARM! CPU value {x}% has been reached")
                            Logger.logger_save_alarm_reached("CPU", x)
                            if platform == "linux" or platform == "linux2":
                                command = ["notify-send", "ALARM! CPU value", f"{x}% has been reached", "--icon=dialog-critical"]
                                Monitor.run_command(command)

                    for x in json_data["DISK"]:
                        if Monitor.DISK() >= int(x):
                            print(f"ALARM! DISK value {x}% has been reached")
                            Logger.logger_save_alarm_reached("DISK", x)
                            if platform == "linux" or platform == "linux2":
                                command = ["notify-send", "ALARM! DISK value", f"{x}% has been reached", "--icon=dialog-crital"]
                                Monitor.run_command(command)

                    for x in json_data["MEMORY"]:
                        if Monitor.MEMORY() >= int(x):
                            print(f"ALARM! MEMORY value {x}% has been reached")
                            Logger.logger_save_alarm_reached("MEMORY", x)
                            if platform == "linux" or platform == "linux2":
                                command = ["notify-send", "ALARM! MEMORY value", f"{x}% has been reached", "--icon=dialog-crital"]
                                Monitor.run_command(command)

                except KeyboardInterrupt:
                    break
