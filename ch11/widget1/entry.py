# entry.py

from tkinter import Tk, Button, Label
from tkinter import Entry
from tkinter import StringVar

otk = Tk()

# (문자열) 변수 값을 위젯과 연결해서 사용
ostring = StringVar()
# textvarialbe : 문자열 값 변화를 자동으로 해당 변수에 반영
oentry = Entry(otk, textvariable = ostring)
obtn = Button(otk, bg = "#07D2EC", command = otk.quit, textvariable = ostring)
olabel1 = Label(otk, bg = "#F0DB24", textvariable = ostring)


otk.geometry("400x300+480+240")
oentry.pack()
obtn.pack()
olabel1.pack()

otk.mainloop()