# tkinter_module.py

# import tkinter

# # 1. 위젯 생성
# otk = tkinter.Tk()
# # obtn = tkinter.Button(otk, command = otk.quit, text = "click")
# obtn = tkinter.Button(otk, text = "click")

# # 2. 위젯 배치
# obtn.pack()

# # 3. 이벤트 바인딩
# # 동작
# otk.mainloop() # 프로그램이 실행 직후 종료되지 않고 유지되게 함 


# from tkinter import *
from tkinter import Tk
from tkinter import Button

def hello():
    print("Hello there")

def talk(txt):
    print(txt)

# 1. 위젯 생성
otk = Tk()
obtn1 = Button(otk, text = "click1", command = hello)
obtn2 = Button(otk, text = "click2", command = lambda:talk("Python"))
obtn3 = Button(otk, text = "click3")

# 2. 위젯 배치
otk.geometry("240x450+400+150",)
# otk.geometry("240x450",)        # 사이즈만 설정
obtn1.pack()
obtn2.pack()
obtn3.pack()

# 3. 이벤트 바인딩
# 동작
otk.mainloop() # 프로그램이 실행 직후 윈도우 창이 종료될 때까지 프로그램이 유지되게 함 
