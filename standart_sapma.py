sayi_grubu=[5,15,20,5,5]

#? Aritmetik Ortalama
a=0
for i in sayi_grubu:
    a+=i

aritmetik_ort=a/len(sayi_grubu)

#? Her veriden aritmetik ortalamayı çıkar

csayi_grubu=[]

for x in sayi_grubu:
    son=x-aritmetik_ort
    csayi_grubu.append(int(son))

#? Sonuçların karelerini al topla
kareler=[]
karelerelemantop=0
for j in csayi_grubu:
    kareler.append(j*j)
for k in kareler:
    karelerelemantop+=k

#? Veri sayısının bir eksiğine böl kare kökünü al

sonuc=karelerelemantop/(len(sayi_grubu)-1)
print(sonuc)
