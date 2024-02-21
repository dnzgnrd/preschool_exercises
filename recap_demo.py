sayi = int(input("Kaç Yıldız Olsun ? "))

yildiz = ""

for x in range(1, sayi+1):
    yildiz = str(yildiz) + "*"
    print(yildiz)

#Asal sayı yazdırma 2,3,5,7,11,13
asal_sayi = int(input("Bir Sayı Giriniz ?"))
asal_mi = "Evet"
for i in range(2, asal_sayi):
    if asal_sayi % i == 0:
        asal_mi = "Hayır"
        break
if asal_mi == "Evet":
    print("ASALDIR!")
else:
    print("ASAL DEĞİLDİR!")




def çarpma_işlemi(a,b):
    return a*b
çarpma = çarpma_işlemi(7,8)
print(çarpma)

































