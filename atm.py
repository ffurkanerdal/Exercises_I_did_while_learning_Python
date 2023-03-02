print("""

atm makinesine hoşgeldiniz
işlemler;
1 bakiye sorgulama
2 para yatırma
3 para çekme

programdan çıkmak için  q


""")

hak=3
bakiye=20000
while True:
    islem=input("işlemi gir")
    if islem=="1":
        print(bakiye)
    elif islem=="2":
        tutar=int(input("tutar gir"))
        bakiye+=tutar
        print(f"güncel bakiyeniz: {bakiye}")
    elif islem=="3":
        tutar=int(input("tutar gir"))
        if tutar>bakiye:
            print("bakiyen yok")
        elif tutar<=bakiye:
            bakiye-=tutar
            print(f"güncel bakiyeniz: {bakiye}")
    elif islem=="q":
        print("sg")
        break
    elif islem!="q" or islem!="Q" or islem!="1" or islem!="2" or islem!="3":
        print("tekrar dene")
        hak-=1
        if hak==0:
            print("sg kolsuz")
            break
