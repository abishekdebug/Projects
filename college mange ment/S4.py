# import tkinter module
from tkinter import *	
from tkinter.ttk import *
root = Tk()

		
root.geometry('2000x2050')	

btn = Button(root, text = ' FIRST YEAR',
				command = root.destroy).place(x = 300, y= 150)


btn1 = Button(root, text = ' SECOND YEAR',
				command = root.destroy).place(x = 600, y= 150)


btn2 = Button(root, text = ' THIRD YEAR',
				command = root.destroy).place(x = 900, y= 150)

btn3 = Button(root, text = ' FINAL YEAR',
				command = root.destroy).place(x = 1200, y= 150)
with open("s5.py") as f:
    exec(f.read())
    



	

root.mainloop()
