import os, requests, sys, time

from datetime import datetime


class Capture:
    def __init__(self, protocol, filter) -> None:
        self.protocol = protocol
        self.connections = os.popen("netstat -at -n").readlines()
        self.Total = 6
        self.filter = filter
    
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
                if Protocol!="TCP":
                    pass
                if "*" in IP:
                    pass
                elif "0.0.0.0" in IP:
                    pass
                elif "127.0.0.1" in IP:
                    pass
                else:
                    if self.Total == 24:
                        pass
                    else:
                        if self.filter == "none":
                            self.display_text(self.Total, 44, Protocol)
                            self.display_text(self.Total, 12, IP.split(":")[0])
                            self.display_text(self.Total, 29, Port)
                            self.display_text(self.Total, 58, State)
                            self.display_text(self.Total, 2, F"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} ")
                            self.Total += 1
                        elif self.filter == "discord":
                            sys.exit()

            except IndexError:
                pass