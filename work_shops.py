#kelime sıralamaca
kelime = input("3 tane kelime giriniz")
yeni_kelime = kelime.split(",")

def liste_sıralama(kelime_listesi):
    kelime_listesi.sort()
    return kelime_listesi

sıralanmıs_kelime= liste_sıralama(yeni_kelime)

print(sıralanmıs_kelime)



sayi = input("3 sayı yaz")
yeni_sayi= sayi.split(",")

print(liste_sıralama(yeni_sayi))





















