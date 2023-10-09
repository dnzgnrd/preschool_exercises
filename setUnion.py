setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)  #union böyle yapılır.
# ya da :
print(setA.union(setB))


# bir de ortak elemanları bulmayı sağlayan intersection fonk. var
print(setA & setB)
#ya da
print(setA .intersection(setB))


#iki set listesi arasındaki farklılıkları yazar A da olup B de olmayan ya da B de olup A da olmayanları verir
print(setA-setB)  #A'nın B'den farkı
print(setB-setA)#B'nin A'dan farkı
#ya da
print(setA.difference(setB)) #A'nın B'den farkı tam tersi şeklinde de yazarsan B'nin A'dan farkını elde edersin

#symmetric set listesi de sadece keşişimlerini yani ortak elemanları yazmıyor geri kalanını yazıyor
#print((setA | setB)-(setA-setB)) bunu ben kendim yazdım normali böyle değil
print(setA ^ setB)
print(setA.symmetric_difference(setB))


