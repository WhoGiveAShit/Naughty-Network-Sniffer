import time

from incoming.connections import *


Platform = os.name
if Platform == "nt":
    os.system("cls")
else:
    os.system("clear")


UI = '''          ┌───────────────┬────────────┬───────────────┬───────────────┐
          │               │            │               │               │
          │IP Address     │   Port     │   Protocol    │   State       │
┌─────────┼───────────────┴────────────┴───────────────┴───────────────┤
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
│         │                                                            │
└─────────┴────────────────────────────────────────────────────────────┘'''


if len(sys.argv) < 2:
    print(UI)
    while True:
        D = Capture("tcp", "none")
        D.display_conns()
else:
    FirstArg = sys.argv[1]
    if FirstArg == "-h":
        print('''python main.py -h || Displays this command\npython main.py || To listen for all ips with no filter\npython main.py <fivem> || To show current fivem connections IE: Server Connections''')
        sys.exit()
    elif FirstArg == "fivem":
        D = Capture("tcp", "fivem")
        D.display_conns()
    elif FirstArg == "portfilter":
        print(UI)
        SecongArg = sys.argv[2]
        while True:
            D = Capture("tcp", SecongArg)
            D.display_conns()
    elif FirstArg == "ignorehttp":
        print(UI)
        while True:
            D = Capture("tcp", "ignorehttp")
            D.display_conns()