import random


pc=7
gamer=0
while True:
    kart=random.randint(1,12)
    sor=input("çek,pas")
    if kart==1:
        print("A")
    elif kart==11:
        print("Q")
    elif kart==12:
        print("K")

    while True:
        if sor=="çek":
            print(kart)
            if kart=="A":
                kart=1
            elif kart=="Q":
                kart=11
            elif kart==12:
                print("K")
