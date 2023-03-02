# Herhangi bir sınıfın veri bilgileri

ogrenci_isim=["Ali","Veli","Sıla","Seda","Ada","Ela","Ece","Efe","Esat","Eda","Seda","Onur","Aslı","Ceyda","Funda"]
ogrenci_soyisim=["Sayan","Bilen","Şahin","Soylu","Musk","Boz","Zorlu","Aslan","Arslan","Malkoçoğlu","Yandanbakan","Soldanbakan","Üsttenbakan","Alttanbakan","Çaprazdanbakan"]
ogrenci_numaralar=[101,202,303,404,505,606,707,808,909,102,203,304,405,506,607]
öğrenci_dersleri=["Fizik","Kimya","Biyoloji","Matematik"]
ogrenci_liste=[]

for i in range(1):
    for j in ogrenci_isim:
        ogrenci_liste.append(j)
    for k in ogrenci_soyisim:
        ogrenci_liste.append(k)
    for x in ogrenci_numaralar:
        ogrenci_liste.append(x)

print(ogrenci_liste)