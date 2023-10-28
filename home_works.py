#Bu dosya sürekli soru çözmek içindir
#dikdörtgen alan ve çevre hesaplama
"""
kisa_kenar = input("kısa kenar uzunluğunu nedir ?")
uzun_kenar = input("uzun kenar uzunluğu nedir ?")
alan_hesaplama = int(kisa_kenar)*int(uzun_kenar)
cevre_hesaplama = 2*(int(kisa_kenar)+int(uzun_kenar))
print("diktörgenin alanı = ",alan_hesaplama)
print("diktörgenin çevresi = ",cevre_hesaplama)

# 2 tane sayı seç ve bu sayıları ortak bölen sayıları yazdır 1ve 100 aralığında
for i in range(1,101):
 if i%3==0 and i%5==0:
    print(i)

sayilar = [50,20,22]
toplam = 0
for i in sayilar:
    toplam=toplam+i
print(toplam)


def toplama_islemi(sayi1,sayi2):
    toplama = sayi1 + sayi2
    print("bu sayıların toplamı=",str(toplama))
toplama_islemi(85,45)



toplama_islemi(100,45)


kullanici_adi = "dnzgnrd03@gmail.com"
sifre = 123456789
bilgiler = input("Kullanıcı Adınızı Giriniz")
bilgiler2 = input("Şifrenizi Giriniz")
def kullanici_giris_kontrol (ad , sifre):
    if kullanici_adi == "dnzgnrd03@gmail.com." and sifre == 123456789:
        print("Hoşgeldiniz")
    else:
        print("Yanlış Kullanıcı Adı Veya Şifre Girdiniz!")



kullanici_giris_kontrol(kullanici_adi,sifre)

"""


#en büyük sayıyı bulma

"""
numbers = input("5 adet sayı giriniz!")
newNumbers = numbers.split(",")

en_buyuk = newNumbers[0]

for i in newNumbers:

    if i>en_buyuk:
       en_buyuk = i
print("en büyük sayı=",en_buyuk)
"""




names = input("3 tane isim giriniz!")
new_names = names.split(",")
new_names.sort()
for name in new_names:
    print(name)


for i in range(5):
    for j in range(5):
      print(j)




























