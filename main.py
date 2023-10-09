#tek sayı yazdırma
sayilar = []

for sayi in range(11, 32):
    if sayi % 2 == 1:
        sayilar.append(sayi)
print(sayilar)

def büyük_harfe_cevir(metin):
    print(metin.upper())
büyük_harfe_cevir("deniz")

sozluk = {
        "Book":"Kitap",
         "Class":"Sınıf",
         "Computer":"Bilgisayar"
         }
print(sozluk)

print(sozluk["Book"])
sozluk["Book"] = "Roman"
print(sozluk)
sozluk["Keyboard"] = "Kılavye"
print(sozluk)

'''
sayi =input("5 Basamaklı Bir Sayı Giriniz ? ")
toplam = 0
for i in sayi:
    toplam =toplam+int(i)
print(toplam)
'''

sayilar = [144,154,4]
sayilar.sort()
sayilar.reverse()
print("en büyük ile ortanca sayının farkı",int(sayilar[0]-sayilar[1]))
print("en büyük ile en küçük sayının farkı",int(sayilar[0]-sayilar[2]))



#Rastgele 600 adet 0 ile 1000 arasında sayı oluşturup bir liste içerisine aktaran ve 100’den küçük olan sayıların adedini ekrana yazdıran python kodlarını yazınız?


sinav1 = int(input("İlk Sınav Notunuzu Giriniz"))
sinav2 = int(input("İkinci Sınav Notunuzu Giriniz"))
ort = (sinav1+sinav2)/2

if ort >=50:
    print("Geçtiniz")
else:
    print("Kaldınız")




























