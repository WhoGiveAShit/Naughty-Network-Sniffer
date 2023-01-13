import time

from incoming.connections import *
os.system("cls")

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
        time.sleep(1)
        D = Capture("tcp", "none")
        D.display_conns()
else:
    FirstArg = sys.argv[1]

    if FirstArg == "-h":
        print('''python main.py -h || Displays this command\npython main.py || To listen for all ips with no filter\npython main.py <discord> || To show current discord connections IE: Voice chats''')
        sys.exit()
    elif FirstArg == "fivem":
        print(UI)
        while True:
            time.sleep(5)
            D = Capture("tcp", "fivem")
            D.display_conns()