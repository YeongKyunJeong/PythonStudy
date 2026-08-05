# option.py

from tkinter import Tk, StringVar
from tkinter import OptionMenu

otk = Tk()
otk.geometry("400x300")

option_list = ['Option1', 'Option2', 'Option3']
selected_option = StringVar()
selected_option.set(option_list[0])

option_menu = OptionMenu(otk, 
                         selected_option, 
                         *option_list)
option_menu.pack()

otk.mainloop()