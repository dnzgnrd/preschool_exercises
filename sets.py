studentsSets = {"Deniz","Eylem","Ümüt","ırmak","Azad"}  #çalıştırdığında dikkat edersen yazdığın sıraya gçre yazmayacak setsler kendi sırasına göre yazar.
#listede var olan bi veriyi değiştiremezsin mesela denizi artık ebru olarak yazdırmak istesen yapamazsın
#ama yeni bir eleman ekleyebilirsin add fonk. ile

for i in studentsSets:
    print(i)
print("Deniz" in studentsSets)

if "Deniz" in studentsSets:
    print("listede Var")

studentsSets.add("Derin")
print(studentsSets)
#birden fazla elelman eklmek istediğinde update fonk. kullanılır
studentsSets.update(["Kiraz","Elma"])
print(studentsSets)

print(len(studentsSets))

studentsSets.remove("Kiraz")
print(studentsSets)

studentsSets.clear()
print(studentsSets)


#del studentsSets  buda seti tamamen siliyo
#print(studentsSets)











