# img_label.py

from tkinter import Tk, Button, PhotoImage, Label
from PIL import Image, ImageTk

otk = Tk()
otk.geometry("680x1000")

# img = PhotoImage(file = "C:/Users/jjbyk/Downloads/pexels-fotodruk-38464218.png")
# img = PhotoImage(file = "ch11/widget2/pexels-fotodruk-38464218.png")
# pil_image = Image.open("C:/Users/jjbyk/Downloads/9d1b6a4bef33ddf2dafb9970cae8c205.jpg")
pil_image = Image.open(r"C:\Users\jjbyk\Downloads\9d1b6a4bef33ddf2dafb9970cae8c205.jpg")
img = ImageTk.PhotoImage(pil_image)
img_label = Label(otk, image = img)
obtn1 = Button(otk, text = "PUSH1")
obtn2 = Button(otk, text = "PUSH2")
obtn3 = Button(otk, text = "PUSH3")

img_label.place(x = 20, y = 20)
obtn1.place(x = 10, y  = 60)
obtn2.place(x = 140, y  = 60)
obtn3.place(x = 80, y  = 10)

otk.mainloop()