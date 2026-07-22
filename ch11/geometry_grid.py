# geometry_grid.py

from tkinter import Tk, Button 

otk = Tk()
otk.geometry("200x100")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.grid(row = 1, column = 0)
obtn2.grid(row = 1, column = 1, padx = 20, pady= 10)
obtn3.grid(row = 0, column = 4)

otk.mainloop()