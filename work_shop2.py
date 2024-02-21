#faktöriyel hesaplama
sayi=int(input("sayı: "))

faktoriyel = 1
if sayi<0:
    print("negatif sayıların faktöriyeli hesaplanamaz. ")
elif (sayi == 0):
    print("sonuç:1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
print("sonuç : ",faktoriyel)


#matris toplama
""""
2 3 4
5 7 8
1 8 7

1 3 2
9 6 8
1 0 7
"""

x = [[2,3,4],[5,7,8],[1,8,7]]
y = [[1,3,2],[9,6,8],[1,0,7]]
sonuc= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j] + y[i][j]
print(sonuc)













#kelime sıralamaca
cumle="bugün hava çok güzel"
kelimeler=cumle.split()
kelimeler.sort()
print(kelimeler)
for kelime in kelimeler:
    print(kelime)


























