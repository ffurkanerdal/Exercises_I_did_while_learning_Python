
#! Kullanıcıdan aldığınız sayının mükkemmel olup olmadığına bakın

#* Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükkemmel sayı" denir. Örnek olarak, 6 mükkemmek bir sayıdır(1+2+3=6)

def muk():
    bolenler=[]
    for i in range(1,sayi):
        if sayi%i==0:
            bolenler.append(i)
    a=0
    for j in bolenler:
        a+=j
    if a==sayi:
        print("sayı mükkemel")
    else:
        print("sayı mükemmel değil")

while True:
    sayi=int(input("sayı gir"))
    muk()
    if sayi==0:
        break