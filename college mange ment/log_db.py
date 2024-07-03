import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    password="@actionabi123",
    database="raja"
)
mycursor = mydb.cursor()
mycursor.execute("select*from reg")
myresult = mycursor.fetchall()
for x in myresult:
    print(x[1])
    
