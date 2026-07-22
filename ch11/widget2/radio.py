# radio.py

from tkinter import Tk, Button
from tkinter import Radiobutton, IntVar

def buy():
    if radio_value.get() in lunch:
        print(f"{lunch[radio_value.get()]}를 주문했습니다.")

otk = Tk()
otk.geometry("200x100")

radio_value = IntVar()      # 정수형 변수 생성
radio_value.set(-1)          # 초기값에 따라 처음 선택된 요소 변경
lunch = {0: "A런치", 1: "B런치", 2: "C런치"}

orb1 = Radiobutton(otk, text = lunch[0], variable = radio_value, value = 0)
orb2 = Radiobutton(otk, text = lunch[1], variable = radio_value, value = 1)
orb3 = Radiobutton(otk, text = lunch[2], variable = radio_value, value = 2)
obtn = Button(otk, text = "주문", command = buy)

orb1.pack()
orb2.pack()
orb3.pack()
obtn.pack()


otk.mainloop()