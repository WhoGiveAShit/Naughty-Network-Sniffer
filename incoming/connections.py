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
    
    def display_information(self, number, Protocol, IP, Port, State, Color):
        self.display_text(number, 44, F"{Protocol}  ")
        self.display_text(number, 12, F"{IP}  ")
        self.display_text(number, 29, F"{Port}    ")
        self.display_text(number, 58, F"{Color}{State}{Fore.WHITE}  ")
        self.display_text(number, 2, F"{PurpleColor}{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}{Fore.WHITE} ")

    def display_conns(self):
        for i in self.connections:
            try:
                Protocol = i.strip().split()[0]
                IP = i.strip().split()[2]
                Port = IP.split(":")[1]
                State = i.split()[3]
                if self.Total == 24:
                    pass
                else:
                    if Protocol!="TCP":
                        pass
                    if "*" in IP:
                        pass
                    if "[" in IP:
                        pass
                    elif "0.0.0.0" in IP:
                        pass
                    elif "127.0.0.1" in IP:
                        pass
                    elif "192.168.0.1" in IP:
                        pass
                    else:
                        if State == "TIME_WAIT":
                            COLOR = "\u001b[38;5;208m"
                            self.display_text(self.Total, 74, F"{Fore.YELLOW}Waiting       {Fore.WHITE}")
                        elif State == "CLOSE_WAIT":
                            COLOR = "\u001b[38;5;196m"
                            self.display_text(self.Total, 74, F"{Fore.YELLOW}Disconnecting{Fore.WHITE}")
                        elif State == "ESTABLISHED":
                            COLOR = "\u001b[38;5;82m"
                            self.display_text(self.Total, 74, F"{Fore.GREEN}Connected{Fore.WHITE}    ")
                        elif State == "LAST_ACK":
                            self.display_text(self.Total, 74, F"{Fore.YELLOW}Disconnecting{Fore.WHITE}")
                        else:
                            COLOR = "\u001b[38;5;231m"
                        if self.Total == 24:
                            pass
                        else:
                            if self.filter == "none":
                                RealIP = IP.split(":")[0]
                                self.display_information(self.Total, Protocol, RealIP, Port, State, COLOR)
                                self.Total += 1
                            elif self.filter == "fivem":
                                RealIP = IP.split(":")[0]
                                if Port == "30120":
                                    self.display_information(self.Total, Protocol, RealIP, Port, State, COLOR)
                                    self.Total += 1
                                else:
                                    pass
                            elif self.filter == "ignorehttp":
                                RealIP = IP.split(":")[0]
                                if Port == "443":
                                    pass
                                elif Port == "80":
                                    pass
                                else:
                                    self.display_information(self.Total, Protocol, RealIP, Port, State, COLOR)
                                    self.Total += 1
                            else:
                                RealIP = IP.split(":")[0]
                                if Port == self.filter:
                                    self.display_information(self.Total, Protocol, RealIP, Port, State, COLOR)
                                    self.Total += 1
                                else:
                                    pass
            except IndexError:
                pass