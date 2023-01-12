import time

from incoming.connections import *

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

FirstArg = sys.argv[1]
if FirstArg == "-h":
    print('''python main.py -h || Displays this command\npython main.py || To listen for all ips with no filter\npython main.py <discord> || To show current discord connections IE: Voice chats''')
    sys.exit()
elif FirstArg == "discord":
    print(UI)
    while True:
        time.sleep(5)
        D = Capture("tcp", "discord")
        D.display_conns()
else:
    print(UI)
    while True:
        time.sleep(1)
        D = Capture("tcp", "none")
        D.display_conns()