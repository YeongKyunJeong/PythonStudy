# assignment.py

# from tkinter import Tk, Label, Checkbutton, Button, BooleanVar, StringVar
# def order():
#     sum = 0
#     text = "주문내역:" 
#     for i in checks:
#         if checks[i].get():
#             text += "\n- " + pizzas[i]
#             sum += prices[i]
#     text += "\n\n총 가격: " + str(sum) +"원"
#     ostr.set(text)
# otk = Tk()
# olabel1 = Label(otk, text = "피자")
# otk.geometry("400x300")
# otk.title("조각 피자 주문 프로그램")
# olabel1.pack()
# pizzas = {0: "치즈 피자 (3200원)", 1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
# prices = {0: 3200, 1: 3500, 2: 3600}
# checks = {}
# for i in pizzas:
#     checks[i] = BooleanVar()
#     ocheck = Checkbutton(otk, text = pizzas[i], variable = checks[i])
#     ocheck.pack(anchor = "w")
# obutton = Button(otk, text = "주문", command = order)
# obutton.pack()
# ostr = StringVar()
# olabel2 = Label(otk, textvariable = ostr)
# olabel2.pack()
# otk.mainloop()


from tkinter import Tk, Checkbutton, Button, BooleanVar, StringVar, Label

def buy():
    text = ""
    for i, coffee in enumerate(coffees):
        if orders[i].get() :
            text += f"{coffee} : {coffees[coffee]}원 \n"
    text = text.strip()
    result.set(text)

otk = Tk()
otk.title("커피머신")
otk.geometry("200x300+150+100")
# otk.geometry("600x700+150+100")

orders = {}
coffees = {"아메리카노" : 3000, "카페라떼" : 4500, "에스프레소" : 2500}
for i, coffee in enumerate(coffees):
    orders[i] = BooleanVar()
    checkbtn = Checkbutton(otk, text = f"{coffee} : {coffees[coffee]} 원", variable = orders[i])
    checkbtn.pack(anchor = 'w')

btn = Button(otk, text = "주문", width = 8, command = buy)
result = StringVar()
btn.pack()
label = Label(otk, textvariable = result, width = 20, height = 3, bg = "#12A1F4")
label.pack(pady = 5)
otk.mainloop()