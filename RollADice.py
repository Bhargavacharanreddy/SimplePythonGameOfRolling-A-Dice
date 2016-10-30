__author__ = 'charan'
loopExit=0;
while loopExit!="q":
    import random
    print("This is Dice Rolling Program");
    print("Press Enter to roll");
    input()
    number=random.randint(1,6)
    if number==1:
        print("[------------]")
        print("[            ]")
        print("[     0      ]")
        print("[            ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()
    if number==2:
        print("[------------]")
        print("[            ]")
        print("[  0    0    ]")
        print("[            ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()
    if number==3:
        print("[------------]")
        print("[  0      0  ]")
        print("[     0      ]")
        print("[            ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()
    if number==4:
        print("[------------]")
        print("[  0    0    ]")
        print("[  0    0    ]")
        print("[            ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()
    if number==5:
        print("[------------]")
        print("[  0     0   ]")
        print("[     0      ]")
        print("[  0     0   ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()
    if number==6:
        print("[------------]")
        print("[  0    0    ]")
        print("[  0    0    ]")
        print("[  0    0    ]")
        print("[------------]")
        print("Press q to exit")
        loopExit=input()

