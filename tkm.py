import random 


liste=["taş","kağıt","makas"]


print("""

        **** Taş/Kağıt/Makas Oyununa Hoşgeldiniz****
                    Çıkış için: 0
""")
pc=0
gam=0
while True:
    bc=random.choice(liste)
    gamer=str(input("veri seçenek yazınız"))

    if bc==gamer:
        print("berabere")
        continue
    elif bc=="taş" and gamer=="makas":
        pc+=1
        print("bilgisayar kazandı bilgisayarın puanı: ",pc,"Oyuncunun puanı: ",gam)
    
    elif bc=="kağıt" and gamer=="taş":
        pc+=1
        print("bilgisayar kazandı bilgisayarın puanı: ",pc,"Oyuncunun puanı: ",gam)
    
    elif bc=="makas" and gamer=="kağıt":
        pc+=1
        print("bilgisayar kazandı bilgisayarın puanı: ",pc,"Oyuncunun puanı: ",gam)
    
    elif gamer=="kağıt" and bc=="taş":
        gam+=1
        print("oyuncu kazandı oyuncunun puanı: ",gam,"bilgisayarın puanı: ",pc)
    
    elif gamer=="makas" and bc=="kağıt":
        gam+=1
        print("oyuncu kazandı oyuncunun puanı: ",gam,"bilgisayarın puanı: ",pc)
    
    elif gamer=="taş" and bc=="makas":
        gam+=1
        print("oyuncu kazandı oyuncunun puanı: ",gam,"bilgisayarın puanı: ",pc)
    
    elif gamer=="çıkış":
        print(f"""

            Oyuncu skoru: {gam}

            Bilgisayar skoru: {pc}    
            
        """)
        if gam>pc:
            print("Tebrikler")
        elif gam<pc:
            print("Bir dahaki sefere")
        else:
            print("berabere")

        break