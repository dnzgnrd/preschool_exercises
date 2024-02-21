"""
import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("select * from customers")
for row in cursor:
    print("First Name: ",row[1])


import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("select city ,count(*) from customers group by city")
for row in cursor:
    print("city: ",row[0])
    print("count: ",str(row[1]))




import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("select city ,count(*) from customers group by city having count(*)>1 order by count(*)desc")
for row in cursor:
    print("city: ",row[0])
    print("count: ",str(row[1]))

"""
import sqlite3
def insertCustomer():
   connection = sqlite3.connect("chinook.db")
   connection.execute("""insert into customers("FirstName","LastName",email,city)values('Deniz','Güngördü','geforce@gmail.com','Tunceli')""")
   connection.commit()
   connection.close()
#insertCustomer()



#update işlemi

import sqlite3
def updateCustomer():
   connection = sqlite3.connect("chinook.db")
   connection.execute("""update customers set city='Tunceli' where city='oslo'""") #ilk önce yapmak istediğini sonra değiştirmek istediğini yaz
   connection.commit()
   connection.close()
#updateCustomer()




#delete işlemi
import sqlite3
def deleteCustomer():
   connection = sqlite3.connect("chinook.db")
   connection.execute("""Delete from customers where customerid=30""") #ilk önce yapmak istediğini sonra değiştirmek istediğini yaz
   connection.commit()
   connection.close()
deleteCustomer()


def joinOperasyonu():
   connection = sqlite3.connect("chinook.db")
   cursor = connection.execute("""select Albums.Title, Artists.Name 
                                   from Artists 
                                   inner join Albums on Artists.ArtistId = Albums.ArtistId""")
   for row in cursor:
      print("Title: ", row[0] ,"Name :",row[1] )

joinOperasyonu()















