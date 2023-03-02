alfabe=["a","b","c","d","e","f","g","h","ı","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
metin=input("Metin giriniz")
sasa=""
for x in range(len(alfabe)):
    for j in alfabe:
        for k in metin:
            x=j
            if j==k:
                ada=alfabe.index(j)
                sasa+=(alfabe[ada+5])

print(sasa)