def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2



print("Operasyon?")
print("1:Topla")
print("2:Çıkar")
print("3:Çarp")
print("4:Böl")

secenek = input("operasyon seçiniz")
sayi1 = int(input("1. sayıyı gir"))
sayi2 = int(input("2. sayıyı gir"))

if secenek == "1":
    print("toplam: ",(topla(sayi1,sayi2)))
elif secenek=="2":
    print("cikar: ",(cikar(sayi1, sayi2)))

elif secenek=="3":
    print("carpma: ",(carp(sayi1, sayi2)))

elif secenek=="4":
    print("böl: ",(bol(sayi1, sayi2)))

else:
    print("geçersiz seçenek")







