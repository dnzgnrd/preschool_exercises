try:
    sayi = int(input("Bir Sayı Giriniz"))
except ValueError:
    print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz")
except ZeroDivisionError:
    print("Payda Sıfır Olmaz")
except:
    print("Bir Hata Oluştu")
print("Bitti")




























