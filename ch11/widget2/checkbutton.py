# checkbutton.py

from tkinter import Tk, Button
from tkinter import Checkbutton, BooleanVar

def buy():
    for i in check_values:
        if check_values[i].get():
             print(f"{coffee[i]}를 주문했습니다.")

otk = Tk()
otk.geometry("100x140")

check_values = {}      # 정수형 변수 생성
coffee = {0: "아메리카노", 1: "라떼", 2: "카푸치노", 3: "에스프레소"}

for i in range(len(coffee)):
    check_values[i] = BooleanVar()
    ocheck = Checkbutton(otk, text = coffee[i], variable = check_values[i])

    ocheck.pack(anchor = "w")

obtn = Button(otk, text = "주문", command = buy)

obtn.pack()


otk.mainloop()