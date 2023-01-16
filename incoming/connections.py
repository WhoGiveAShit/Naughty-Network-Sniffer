import os, requests, sys, time, socket, urllib.request

from datetime import datetime
from colorama import Fore, init
from urllib.request import Request, urlopen


init()
PurpleColor = '\033[93m'
locations = []

class Capture:
    def __init__(self, protocol, filter) -> None:
        self.protocol = protocol
        self.connections = os.popen("netstat -at -n").readlines()
        self.Total = 6
        self.filter = filter
        Platform = os.name
        if Platform == "nt":
            os.system(f"title Filter - {filter}")
        else:
            pass
    
    def display_text(self, x, y, text):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
    
    def display_information(self, number, Protocol, IP, Port, State, Color):
        locations.append(F"{number}, 10:{IP}")
        self.display_text(number, 44, F"{Protocol}  ")
        self.display_text(number, 12, F"{IP}  ")
        self.display_text(number, 29, F"{Port}    ")
        self.display_text(number, 58, F"{Color}{State}{Fore.WHITE}  ")
        self.display_text(number, 2, F"{PurpleColor}{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}{Fore.WHITE}")

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
                        elif State == "FIN_WAIT_2":
                            COLOR = "\u001b[31m"
                            self.display_text(self.Total, 74, F"{Fore.LIGHTRED_EX}Disconnected  {Fore.WHITE}")
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
                                    if State == "ESTABLISHED":
                                        req = Request(
                                        url=f'http://{RealIP}:{Port}', 
                                        headers={'User-Agent': 'Mozilla/5.0'}
                                        )
                                        response = urllib.request.urlopen(req).read().decode()
                                        data = open("data.txt", "w")
                                        data.write(response)
                                        data.close()
                                        read_data = open("data.txt", "r")
                                        read_data_lines = read_data.readlines()
                                        user_information = []
                                        server_information = []
                                        playerid = 0
                                        for line in read_data_lines:
                                            if "fivem://connect/cfx.re/join" in line:
                                                connect_code = line.strip().replace("location.href = '", "").replace("';", "").replace("fivem://connect/cfx.re/join/", "")
                                                try:
                                                    linker = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{connect_code}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'})
                                                except:
                                                    os.system("cls")
                                                    print("There was an error contacting the server!")
                                                    sys.exit()
                                                try:
                                                    userdata = str(linker.json()["Data"]["clients"])
                                                    maxclients = str(linker.json()["Data"]["sv_maxclients"])
                                                    amount = ''.join(maxclients)
                                                    for i in range(int(amount)):
                                                        try:
                                                            userinformation = str(linker.json()["Data"]["players"][playerid]["name"])
                                                            user_information.append(userinformation)
                                                            playerid += 1
                                                        except:
                                                            break
                                                    real_user_data = ''.join(userdata)
                                                except:
                                                    pass
                                            else:
                                                pass
                                        self.display_text(2, 2, F"Server connect code - {connect_code}\nServer IP - {RealIP}\nPeople within server - {real_user_data}\nPlayer information - {user_information}")
                                        try:
                                            os.remove("data.txt")
                                        except:
                                            pass
                                        break
                                    else:
                                        self.display_text(2, 2, "No server Detected!")
                                        time.sleep(1.5)
                                        pass
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