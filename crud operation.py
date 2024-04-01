import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sdb")
cursor=connection.cursor()
#cursor.execute("create database sdb")
#cursor.execute("use sdb")
#cursor.execute("create table tb1(sno int auto_increment not null primary key,name varchar(50),age int,address varchar(50))")
'''s="insert into tb1(name,age,address) values (%s,%s,%s)"
t=[("Deeban",23,"TVR"),("subi",21,"Myd"),("subha",22,"Myd")]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid) '''
cursor.execute("select * from tb1")
result=cursor.fetchall()
print("content in the python: ",result)
#sql="DELETE FROM tb1"
#cursor.execute(sql)
#print("all rows are deleted")
sql="update tb1 set name='Deepika' where sno=30"
cursor.execute(sql)
connection.commit()