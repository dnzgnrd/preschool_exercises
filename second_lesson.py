mesaj = "Deniz Güngördü"
#burada yaptığın şey sadece harfi yazdırmak
print(mesaj[2:5])
yeniMesaj=mesaj[13:14]
print(yeniMesaj)

#mesajın uzunluğu belli değil ve en son harfini yazdırmak istersek len fonk. kullanıcaz
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#harfleri küçük yazmak için lower kullanılır
print(mesaj.lower())
#harfleri büyük yazmak için upper kullanılır
print(mesaj.upper())

#eğer harf değiştirmek istersem replace fon. kullanıcam
print(mesaj.replace("ü","u"))
print(mesaj.replace("e","a"))

#split fonk. yazdığın yazıyı neye göre ayıracağını belirler
bilgi = "Deniz Güngördü 21"
print(bilgi.split())

bilgi = "Deniz.Güngördü.21"
print(bilgi.split("."))
#spliti bir de bu yazının içinden hangisini yanlızca yazmak istersen indeksini yazınca direk kelime olarak yazıcak
bilgi = "Deniz Güngördü 21"
print(bilgi.split()[2])

#bir de strip diye bişey var o da fazlalıkları özel karakterleri falan siliyo

bilgi = "     Deniz Güngördü 21".strip()
print(bilgi.split())

#kullanıcıdan bilgi almak için input fonk. kullanılır ve metinsel veriler için kullanılır eğer sayısal işlem yapacaksan int ile kullanmalısın
ad = input("lütfen Adınızı Giriniz")
print("hoşgeldin",ad)

sayi1 = input("sayı 1 = ?")
sayi2 = input("sayı 2 = ?")
print(int(sayi1)+int(sayi2))

