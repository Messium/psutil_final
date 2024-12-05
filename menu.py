import os

from alarm import Alarm
from ansi import Ansi
from delete_alarm_json import Delete_alarm
from logger import Logger
from monitor import Monitor
from utils import Utils


class Menu():

    options = {
        "1": ["Start monitor"],
        "2": ["List active monitor"],
        "3": ["Create alarms"],
        "4": ["Show alarms"],
        "5": ["Monitor mode"],
        "6": ["Delete alarms"],
        "7": ["Exit"]
    }

    @staticmethod
    def menu_startup():
        while True:
            try:
                print(Utils.welcome_message())

                for key, value in Menu.options.items():
                    menu_print = f"{Utils.pointer()} {Ansi.RED} {key} {Ansi.END} {value[0]}"
                    print(menu_print)

                user_input = input()

                if user_input == "1":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │          Startar övervakning av CPU användning,          │
                    #          │    minnesanvändning och diskanvändning. Notera alltså    │
                    #          │     att ingen övervakning ska starta automatiskt vid     │
                    #          │                      programstart.                       │
                    #          ╰──────────────────────────────────────────────────────────╯
                    Monitor.start_monitor()

                elif user_input == "2":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │   Listar aktiv övervakning som är aktiv samt nuvarande   │
                    #          │         övervakningsstatus. Har man inte startat         │
                    #          │      övervakningen ska en text visas som informerar      │
                    #          │   användaren om att ingen övervakning är aktiv. Annars   │
                    #          │      visas övervakningen, t.ex: CPU Anvädning: 35%       │
                    #          │     Minnesanvändning: 65% (4.2 GB out of 8 GB used)      │
                    #          │  Diskanvändning: 80% (400 GB out of 500 GB used) Efter   │
                    #          │    detta promtas användaren om att bekräfta genom att    │
                    #          │      trycka enter. Tryck valfri tangent för att gå       │
                    #          │      tillbaka till huvudmeny Efter detta visas åter      │
                    #          │                huvudmenyn för användaren.                │
                    #          ╰──────────────────────────────────────────────────────────╯
                    Alarm.active_alarms()

                elif user_input == "3":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │   Väljer man detta alternativ får man upp ytterligare    │
                    #          │   en meny där man får välja att konfigurera larm inom    │
                    #          │      tre områden eller gå tillbaka till huvudmenyn.      │
                    #          │          Konfigurera larm 1. CPU användning 2.           │
                    #          │   Minnesanvändning 3. Diskanvändning 4. Tillbaka till    │
                    #          │   huvudmeny Efter att man valt ett alternativ får man    │
                    #          │   välja en procentuell nivå där larmet ska aktiveras.    │
                    #          │    T.ex. Ställ in nivå för alarm mellan 0-100. Efter     │
                    #          │        att användaren har valt en nivå skrivs en         │
                    #          │  bekräftelse ut, sedan visas huvudmenyn igen. Larm för   │
                    #          │   CPU användning satt till 80%.  Nivån måste matas in    │
                    #          │   som en siffra mellan 1-100 och matas nonsens in ska    │
                    #          │             användaren få ett felmeddelande.             │
                    #          ╰──────────────────────────────────────────────────────────╯
                    Alarm.create_alarms()

                elif user_input == "4":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │     Listar alla configurerade larm. Larmen ska vara      │
                    #          │   sorterade på typ när de visas. Exempel: 1. CPU larm    │
                    #          │ 70% 2. Disklarm 95% 3. Minneslarm 80% 4. Minneslarm 90%  │
                    #          │   Efter detta promtas användaren om att bekräfta genom   │
                    #          │    att trycka enter. Tryck valfri tangent för att gå     │
                    #          │   tillbaka till huvudmeny Notera att man kan ha flera    │
                    #          │                    larm av samma typ.                    │
                    #          ╰──────────────────────────────────────────────────────────╯
                    Alarm.show_alarms()

                elif user_input == "5":
                    #       ╭────────────────────────────────────────────────────────────────╮
                    #       │                 Startar ett övervakningsläge.                  │
                    #       │ Användaren blir promtad om att övervakningsläget har startats, │
                    #       │    sedan loopar en sträng med jämna mellanrum som meddelar     │
                    #       │                           användaren                           │
                    #       │     att övervakningen är aktiv samt att man kan trycka på      │
                    #       │                          valfri knapp                          │
                    #       │                för att återgå till huvudmenyn.                 │
                    #       ╰────────────────────────────────────────────────────────────────╯
                    Monitor.monitor_mode()

                elif user_input == "6":
                    Delete_alarm.delete_alarm()

                elif user_input == "exit" or user_input == "7":
                    break
                else:
                    os.system('clear')
                    print(
                        f"Please choose an numbered option between 1 and {len(Menu.options)}")
            except KeyboardInterrupt:
                break


Logger.logger()
json_data = Utils.read_alarms_json()
Menu.menu_startup()
