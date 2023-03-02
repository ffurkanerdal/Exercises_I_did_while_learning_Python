# sayı tahmin oyunu

import random

print("""

                    ****Sayı Tahmin oyununa hoşgeldniz****

                            1-Basit (1,10)
                            2-Orta  (1,50)
""")


while True:
    eylem=int(input("eylemi gir"))
    if eylem == 1:
        print("1. Seviyeye girmiş bulunmaktasınız 10 adet yanlış tahmin hakkınız olacaktır bol şanslar (çıkış için 0)")
        hak=10
        dyanıt=0
        while True:
            tahmin=int(input("sayı giriniz"))
            sayi=random.randint(1,10)
            if dyanıt == 10:
                print("tebrikler")
                dyanıt=0
                break

            elif tahmin==0:
                print("bildiğiniz soru sayısı: ",dyanıt)
                break

            elif hak==0:
                print("hakkınız bitmiştir...")
                break

            elif tahmin == sayi:
                dyanıt+=1
                print("Tebrikler doğru yanıt bildiğiniz soru sayısı: ",dyanıt)
        
            elif tahmin != sayi:
                hak-=1
                print("yanlış cevap kalan hakkınız: ",hak)
        
    elif eylem==2:
        dyanıt=0
        hak1=20
        while True:
            print("2. Seviyeye girmiş bulunmaktasınız 20 adet yanlış tahmin hakkınız bulunmaktadır bol şans (çıkış=0)")
            tahmin=int(input("sayı giriniz"))
            sayi=random.randint(1,50)
            if dyanıt==10:
                print("tebrikler")
            
            elif tahmin==0:
                break

            elif hak1==0:
                print("doğru yanıt sayınız",dyanıt)
                dyanıt=0
                break

            elif tahmin==sayi:
                dyanıt+=1
                print("tebrikler doğru yanıt bildiğiniz soru sayısı: ",dyanıt)
            
            elif tahmin != sayi:
                hak1-=1
                print("yanlış cevap kalan hakkınız: ",hak1)
    elif eylem==0:
        break
