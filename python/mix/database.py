import mysql.connector

conn = mysql.connector.Connect( host="127.0.0.1", user='root',password='')

mySqlAddress = conn.cursor()

# mySqlAddress.execute("CREATE DATABASE mydb_saini")
# myInsert= "INSERT INTO "


myselect = "show databases"

a=mySqlAddress.execute(myselect)

print(a);


conn.close()

