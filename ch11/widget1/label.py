# label.py

from tkinter import *
otk = Tk()

# width 단위: 문자 폭
# olabel1 = Label(otk, text = "코랄", bg = "coral", width = 10)
# olabel1 = Label(otk, text = "코랄", bg = "#FFFFFF", width = 10)
olabel1 = Label(otk, text = "코랄", bg = "coral", width = 10)
olabel2 = Label(otk, text = "스프링그린", bg = "springgreen", width = 15)
olabel3 = Label(otk, text = "딥스카이블루", bg = "deepskyblue", width = 20)

otk.geometry("500x300")

olabel1.pack()
olabel2.pack()
olabel3.pack()

otk.mainloop()