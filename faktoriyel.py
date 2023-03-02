

while True:
    try:
        sayi=int(input("sayı gir"))
        if sayi=="q":
            break
        elif sayi<=0:
            print("sg")
            break
        elif sayi==1:
            print(1)
        a=1
        for fak in range(2,sayi+1):
            a*=fak
        print(a)
    except ValueError:
        print("Yanlış değer")