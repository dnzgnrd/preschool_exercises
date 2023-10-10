# diziler     #for ile daha kolay yapılabilir
meyveler = ["Erik", "elma", "kiraz", "kavun"]

print(meyveler)

print(meyveler[0])
print(meyveler[1])
print(meyveler[2])
print(meyveler[3])
print(len(meyveler))

meyveler[2] = "cilek"
print(meyveler)

sayilar = [34, 90, 32, 89, 100]

enBuyuk = sayilar[0]
for sayi in sayilar:

    if sayi > enBuyuk:
        enBuyuk = sayi

print("en büyük sayı", enBuyuk)

#append ve remove fonk listeye yeni eleman eklemek ve var olan elamı silmek için kullanılır
sayilar = [1,2,3]
sayilar.append(5)
sayilar.remove(2)
print(sayilar)

#yada list adı altında liste fonk. açabilirsin örn:
sehirler = list(("İzmir","Ankara","Tunceli"))
print(sehirler)
#clear fonk. kullanarak olan listeyi silebilirsin
#print(sehirler.clear())


#bir de count fonk. var bu da listede hangi elemandan kaç tane olduğunu sayıyor
print("Listede ki Tunceli Sayısı = ",sehirler.count("Tunceli"))

#bu da istediğin elemanın indeksini bulup sana veriyo
print("Listede ki Tunceli şehrinin indexi = ",sehirler.index("Tunceli"))

#indekse göre silme işlemi de pop fonk ile yapılır
sehirler.pop(1)   #pop ın içine bişey yazmassan yani index yazmassan en sondaki elemanı siler
print(sehirler)

#indekse göre ekleme de şu şekilde hangi indekse yerleştirmek istiyosan onu yazıcaksın sonra eklemek istediğin şeyi
sehirler.insert(0,"Antalya")
print(sehirler)

#reverse fonk ise listeyi tersten yazar örnek:
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()
sehirler2 = sehirler
sehirler2[0] = "Manisa"
print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
print(sehirler)






















