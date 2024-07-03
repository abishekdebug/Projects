
from tkinter import *	


from tkinter.ttk import *


root = Tk()
root.geometry('2000x2050')	

btn = Button(root, text = ' CST',
				command = root.destroy,).place(x = 300, y= 150)

btn1 = Button(root, text = ' AD',
				command = root.destroy,).place(x = 600, y= 150)

btn2 = Button(root, text = ' CIVIL',
				command = root.destroy,).place(x = 900, y= 150)
with open("s4.py") as f:
    exec(f.read())


	

root.mainloop()






