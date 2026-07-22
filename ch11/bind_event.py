# bind_event.py

from tkinter import Tk, Button, Entry, StringVar

def order(event):
    print(f"{ostr.get()}을(를) 주문했습니다.")

otk = Tk()
ostr = StringVar()
oentry = Entry(otk, textvariable = ostr)
# obtn = Button(otk, text = "주문", command = order)
obtn = Button(otk, text = "주문", width = 10, height = 3)

otk.geometry("400x300")
oentry.pack()
obtn.pack()

obtn.bind("<Button-1>", order)

otk.mainloop()