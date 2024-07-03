from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd="@actionabi123",
    database='raja')
mycursor = mydb.cursor()

mydb.commit()
top2 = Tk()
top2.geometry("400x450")
name_var = StringVar()
fname_var = StringVar()
dob_var = StringVar()
age_var = StringVar()
add_var = StringVar()
mob_var = StringVar()
def get_data():
    n=name_var.get()
    print(n)
    fn=fname_var.get()
    print(fn)
    dob=dob_var.get()
    print(dob)
    age=age_var.get()
    print(age)
    addres=add_var.get()
    print(addres)
    mob=mob_var.get()
    print(mob)
    quer = "INSERT INTO reg(id, name, fname, dob, age, address, mob) values (%s, %s, %s, %s, %s, %s, %s)"
    val =(0, n, fn, dob, age, addres, mob)
    mycursor.execute(quer,val)
    mydb.commit()
    #call new
    with open("s0.py") as f:
        exec(f.read())

name = Label (top2, text= "Name").place(x= 50, y=50)
fname = Label (top2, text= "fName").place(x= 50, y=90)
dob = Label (top2, text= "dob").place(x= 50, y=130)
age = Label (top2, text= "age").place(x= 50, y=170)
add = Label (top2, text= "add").place(x= 50, y=210)
mob = Label (top2, text= "mob").place(x= 50, y=250)
e1 = Entry(top2,textvariable=name_var).place( x = 120, y = 50)
e2 = Entry(top2,textvariable=fname_var).place( x = 120, y = 90)
e3 = Entry(top2,textvariable=dob_var).place( x = 120, y = 130)
e4 = Entry(top2,textvariable=age_var).place( x = 120, y = 170)
e5 = Entry(top2,textvariable=add_var).place( x = 120, y = 210)
e6 = Entry(top2,textvariable=mob_var).place( x = 120, y = 250)
button=Button(top2, text="submit", fg="red", command=get_data)
button.place(x = 100, y= 350)
top2.mainloop()


