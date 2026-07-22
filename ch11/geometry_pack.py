# geometry_pack.py

from tkinter import Tk, Button

otk = Tk()
otk.geometry("200x100")

obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")
obtn4 = Button(otk, text = "PUSH4")

obtn1.pack(side = 'left')
obtn2.pack(side = 'left')
obtn3.pack(side = 'top')
obtn4.pack(side = 'bottom')

otk.mainloop()