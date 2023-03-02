
#! Kullanıcıdan aldığınız sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

#? Örnek olarak, bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan her birinin 4. kuvvetinin toplamı(3 basamaklı sayılar için 3. kuvveti) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

#? Örnek olarak: 1634= 1^4 + 6^4 + 3^4 + 4^4



def armstrong():
    uzun=len(str(sayi))
    a=0
    for i in str(sayi):
        a+=int(i)**uzun
    if a==sayi:
        print("Sayı Armstrong sayısıdır")
    else:
        print("Sayı Armstrong sayısı Değildir")

while True:
    sayi=int(input("sayı gir:"))
    armstrong()
    if sayi==0:
        break