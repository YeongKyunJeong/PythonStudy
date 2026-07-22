# button.py


from tkinter import Tk, Button 

otk = Tk()
obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

otk.geometry("400x300")
obtn1.pack()
obtn2.pack()
obtn3.pack()

otk.mainloop()