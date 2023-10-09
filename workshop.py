x = 30
if x<10:
  print("10'dan küçük")

else:
  print("10'dan büyük")



sayilar = [6,9,12,15,7]
for i in sayilar:
  if i<10:
   print("10'dan küçük")
  else:
    print("10'dan büyük")


#Python 1-30 arası tek sayıları for döngüsü ile ekrana yazdırınız
#for i in range(1,30,2):
 # print(i)

#Python 50’den 20(dahil ise)’ye kadar olan sayıları 3’er azaltarak for döngüsü ile ekrana yazdırınız.
for i in range(50,19,-3):
  print(i)


numbers = [6,9,8,1]
toplam = 0
for i in numbers:
  toplam= toplam+i
print("tüm sayıların toplamı",toplam)

def mesaj():
  print("su içmeyi unutmayınız")


mesaj()
mesaj()
mesaj()



def isimler(isim,soyisim):
  print("hoşgeldiniz",isim,soyisim)
isimler("deniz","güngördü")
isimler("deniz","güngördü")
isimler("deniz","güngördü")