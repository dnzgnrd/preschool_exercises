tupleListe = (1,2,5,"Deniz",(8,9,7))
liste = [6,8,1,"Hello",()]

liste[0] = 7  #tuple olmayan değişkenleri bu şekilde değiştirebilirsin aynısını tuple için yaparsan eror yersin.
print(liste)

print(liste[-2])
print(tupleListe[-2])  #bu -2 nin olayı da şu en sondaki ikinci eleman demek bunda denizi üstündekinde helloyu yazdıracak

print(liste[1:2])
print(tupleListe[1:2])  #dikkat edersen yanındaki virgülü de yazdırıyo tupple. tuple olduğu belli olsun diye

tupleDeger = ("deniz",) #böyle yazmalısın ki tuple olduğunu anlasın (tek elemanda yapılır bu )
print(type(tupleDeger))

#tuple de ekleme ve çıkarma yok unutmaa



