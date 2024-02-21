import mdouleTest
mdouleTest.topla(2,3)


import mdouleTest as mm
mm.topla(3,5)




print(mm.musteri["firstName"])

# sadece bir fonksiyonu ya da sadece bir class ı dahil etmek istersek:
from mdouleTest import topla
topla(3,7)

from mdouleTest import musteri
print(musteri["firstName"])




