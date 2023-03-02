# kemik oyunu: kemik parçası var ikiye bölünüyor birisi diğerinden büyük küçük olanı seçerse kaybeder


import random



oyuncu=0
pc=0
while True:

    s1=random.randint(0,20)
    s2=random.randint(0,20)
    
    sec=int(input("kemik seç (1 ya da 2) çıkış için: 0"))

    if sec==1:
        if s1>s2:
            oyuncu+=1
            print("......tebrikler.....",f"\nOyuncu: {oyuncu}\nBilgisayar: {pc}")
        else:
            pc+=1
            print(":( :( :( :( :( :( :(",f"\nOyuncu: {oyuncu}\nBilgisayar: {pc}")
    elif sec==2:
        if sec==2:
            if s2>s1:
                oyuncu+=1
                print("......tebrikler.....",f"\nOyuncu: {oyuncu}\nBilgisayar: {pc}")
            elif s1>s2:
                pc+=1
                print(":( :( :( :( :( :( :(",f"\nOyuncu: {oyuncu}\nBilgisayar: {pc}")
    elif sec==0:
        print(f"Oyuncu : {oyuncu}\nBilgisayar : {pc}")
        break