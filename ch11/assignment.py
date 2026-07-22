# assignment.py

from tkinter import Tk, Label, Checkbutton, Button, BooleanVar, StringVar
def order():
    sum = 0
    text = "주문내역:" 
    for i in checks:
        if checks[i].get():
            text += "\n- " + pizzas[i]
            sum += prices[i]
    text += "\n\n총 가격: " + str(sum) +"원"
    ostr.set(text)
otk = Tk()
olabel1 = Label(otk, text = "피자")
otk.geometry("400x300")
otk.title("조각 피자 주문 프로그램")
olabel1.pack()
pizzas = {0: "치즈 피자 (3200원)", 1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
prices = {0: 3200, 1: 3500, 2: 3600}
checks = {}
for i in pizzas:
    checks[i] = BooleanVar()
    ocheck = Checkbutton(otk, text = pizzas[i], variable = checks[i])
    ocheck.pack(anchor = "w")
obutton = Button(otk, text = "주문", command = order)
obutton.pack()
ostr = StringVar()
olabel2 = Label(otk, textvariable = ostr)
olabel2.pack()
otk.mainloop()


