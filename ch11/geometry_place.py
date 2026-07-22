# geometry_place.py

from tkinter import Tk, Button 

otk = Tk()
otk.geometry("200x100")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

obtn1.place(x = 10, y  = 60)
obtn2.place(x = 140, y  = 60)
obtn3.place(x = 80, y  = 10)

otk.mainloop()