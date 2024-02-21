dosya = open("öğrenciler.txt","w")
print(dosya.read())

print(dosya.readline()) #her okuduğu için satır bırakacak ama  sürekli yazman gerek her okuduğunu yazdırması için

for l in dosya:
    print(l)         #her okuduğu için satır bırakıcak bu daha kolay readline a göre
    





















