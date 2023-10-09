sozluk = {
          "book": "kitap",
           "table": "masa"
         }
print(sozluk)


print(sozluk["book"])  #yaparsan anlamını verir sana

#ya da diyelim değiştirmek istersek mesela:
#sozluk["book"] = "kitap 1"
#print(sozluk["book"])


#ekleme yapmak istersen
sozluk["pencil"] = "kalem"
print(sozluk)


#ya da şu şekilde yapacaksın ama genellikle üstteki yapılır.
#sozluk2 = dict (kitap = "book",masa = "table",kalem = "pencil")
#print(sozluk2)

#eğer bi şeyi silmek istersen
del(sozluk["book"])
print(sozluk)
#eleman sayısı öğrenmek için zaten len fonk. kullanılır.
print(len(sozluk))






