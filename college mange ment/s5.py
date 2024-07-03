from tkinter import *	
from tkinter.ttk import *
root = Tk()
root.geometry('1000x1050')	

btn = Button(root, text = ' odd semester',
				command = root.destroy).place(x = 400, y= 150)

btn1 = Button(root, text = ' even semester',
				command = root.destroy).place(x = 900, y= 150)
with open("tree.py") as f:
        exec(f.read())




	

root.mainloop()
