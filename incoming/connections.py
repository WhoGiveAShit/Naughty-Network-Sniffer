import os, requests, sys, time

from datetime import datetime
from colorama import Fore, init

init()
PurpleColor = '\033[93m'

class Capture:
    def __init__(self, protocol, filter) -> None:
        self.protocol = protocol
        self.connections = os.popen("netstat -at -n").readlines()
        self.Total = 6
        self.filter = filter
        os.system(f"title Filter - {filter}")
    
    def display_text(self, x, y, text):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()

    def display_conns(self):
        for i in self.connections:
            try:
                Protocol = i.strip().split()[0]
                IP = i.strip().split()[2]
                Port = IP.split(":")[1]
                State = i.split()[3]
                if State == "TIME_WAIT":
                    COLOR = "\u001b[38;5;208m"
                elif State == "CLOSE_WAIT":
                    COLOR = "\u001b[38;5;196m"
                elif State == "ESTABLISHED":
                    COLOR = "\u001b[38;5;82m"
                else:
                    COLOR = "\u001b[38;5;231m"
                if Protocol!="TCP":
                    pass
                if "*" in IP:
                    pass
                elif "0.0.0.0" in IP:
                    pass
                elif "127.0.0.1" in IP:
                    pass
                elif "192.168.0.1" in IP:
                    pass
                else:
                    if self.Total == 24:
                        pass
                    else:
                        if self.filter == "none":
                            RealIP = IP.split(":")[0]
                            self.display_text(self.Total, 44, F"{Protocol}  ")
                            self.display_text(self.Total, 12, F"{RealIP}  ")
                            self.display_text(self.Total, 29, F"{Port}    ")
                            self.display_text(self.Total, 58, F"{COLOR}{State}{Fore.WHITE}  ")
                            self.display_text(self.Total, 2, F"{PurpleColor}{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}{Fore.WHITE} ")
                            self.Total += 1
                        elif self.filter == "fivem":
                            RealIP = IP.split(":")[0]
                            if Port == "30120":
                                self.display_text(self.Total, 44, F"{Protocol}  ")
                                self.display_text(self.Total, 12, F"{RealIP}  ")
                                self.display_text(self.Total, 29, F"{Port}    ")
                                self.display_text(self.Total, 58, F"{COLOR}{State}{Fore.WHITE}  ")
                                self.display_text(self.Total, 2, F"{PurpleColor}{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}{Fore.WHITE} ")
                                self.Total += 1
                            else:
                                pass
                        else:
                            RealIP = IP.split(":")[0]
                            if Port == self.filter:
                                self.display_text(self.Total, 44, F"{Protocol}  ")
                                self.display_text(self.Total, 12, F"{RealIP}  ")
                                self.display_text(self.Total, 29, F"{Port}    ")
                                self.display_text(self.Total, 58, F"{COLOR}{State}{Fore.WHITE}  ")
                                self.display_text(self.Total, 2, F"{PurpleColor}{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}{Fore.WHITE} ")
                                self.Total += 1
                            else:
                                pass
            except IndexError:
                pass