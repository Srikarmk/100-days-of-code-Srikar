import mysql.connector 

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saisrikar1"
)

mycursor=db.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
