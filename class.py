# en temel amaç bir şeyleri organize etmek birbirleryle ilgili olanları bi class a toplayıp kolayca çağırmak için
#self mimarisi:
class Matematik:
    def topla(self, sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2

    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2

matematik = Matematik()  #böyle yapmamın sebebi Matematik adında belleğimde yer açmam artık belleğimde burdaki işlemler
print("Toplam: ", str(matematik.topla(87, 2)))


#init fonksiyonu:

class Matematik:
    def __init__(self,sayi1,sayi2): #inite sayı1 ve sayi2 yi dahil edip diğerlerinden kaldırınca hepsi için yine çalışacak çünkü zaten hepsi sayı1 ve sayi2 için çalışıyo
        self.sayi1=sayi1
        self.sayi2=sayi2

    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

matematik = Matematik(2,88)  #böyle yapmamın sebebi Matematik adında belleğimde yer açmam artık belleğimde burdaki işlemler
print("Toplam: ", str(matematik.topla()))


#özellik barındıran sınıflarla çalışmak:
class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Deniz" ,"Güngördü",22)
print(person1.firstName)


#miras yapısı:
#worker ve customer için aynı zamanda personda ki last name first name ve age'i karşılamasını istiyorum yani person'dan miras alsınlar.
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary


class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

ayse = Worker()
#buraya gelip ayse. yapınca age last name first name salary credit card number gibi seçenekler çıkacak artık
zeynep = Customer()


























