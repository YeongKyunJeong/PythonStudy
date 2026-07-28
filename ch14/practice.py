# practice.py

# print((lambda x, y : x + y if x + y > 15 else x - y)(7, 1))

# try:
#     raise(KeyError())
# except KeyError:
#     print("Key is missing!")

# try:
#     raise(KeyError("Key is missing!"))
# except KeyError as e:
#     print(e)

import re

# text  = "My phone number is 123-456-7890"
# numbers = re.findall(r"\d+", text)
# print(numbers)

# text = "Contact us at support@example.com or sales@example.org."
# emails = re.findall(r"\w+@\w+\.\w+", text)
# print(emails)

# phone = "123-456-7890"
# phone_pattern = r"\d{3}-\d{3}-\d{4}$"
# print( re.match(phone_pattern, phone))

# import re
# pattern = r'\w+'
# text = "Hello, World!"
# print(re.findall(pattern, text))

# import re
# pattern = r'(ab)+'
# text = "ababab"
# match = re.match(pattern, text)
# print(match.group())

# text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
# import re
# emails = re.findall( r"\w+@\w+\.\w+" , text)
# print(emails)

# text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
# import re
# numbers = re.findall( r"010-\d{3,4}-\d{4}|02-\d{3,4}-\d{4}", text)
# # numbers = re.findall( r"(010|02)-\d{3,4}-\d{4}", text)
# print(numbers)

# text = "I love Python. Java is also popular. Python is great for AI."
# import re
# sentence = re.findall(r"[\w\s]+[.]", text)
# print(sentence)

# text = "상품 코드: A123, B456, C789, 가격: 12000원"
# import re
# prices = re.findall( r"\d+", text)
# print(prices)

# text = "NASA is working on AI projects with IBM and Google."
# import re
# uppers = re.findall(r"[A-Z]{2,}", text)
# print(uppers)


# import math

# fac = math.factorial(5)
# print(fac)

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# baduk = Dog()
# print(baduk.speak())

# import tkinter as tk
# from tkinter import messagebox

# def on_button_click():
#     messagebox.showinfo("알림", "버튼이 클릭되었습니다.")

# root = tk.Tk()
# root.title("간단한 Tkinter 앱")
# root.geometry("300x200")

# btn = tk.Button(root, text = "클릭하세요", command = on_button_click)
# btn.pack(pady=20)

# root.mainloop()


# with open("data.txt", 'w', encoding = 'utf-8') as file:
#     for i in range(1, 11):
#         file.write(f"{i}번째 줄입니다.\n")

# with open("data.txt", "r", encoding = 'utf-8' ) as file:
#     contents = file.read()
#     contents = contents.strip()
# print('파일내용:')
# print(contents)

# with open("data.txt", "a", encoding = 'utf-8') as file:
#     file.write("11번째 줄입니다.")

# with open("data.txt", "r", encoding = 'utf-8' ) as file:
#     contents = file.read()
#     contents = contents.strip()
# print('파일내용:')
# print(contents)

# while True:
#     try:
#         num = input("숫자를 입력하세요.")
#         num = float(num)
#         print(num**2)
#         break
#     except ValueError as e:
#         print("올바른 숫자를 입력하세요!")

# numbers = [10, 20, 30, 40, 50]
# for result in map(lambda x: x**2, numbers):
#     print(result)

# data = """python one
# life is too short
# python two
# you need python
# python three"""

# import re
# sentences = re.findall(r"^python[ \w]+", data, re.M)
# for sentence in sentences:
#     print(sentence)

# import re
# email = "user@example.com"
# result = re.match(r"\w+@\w+[.]\w+", email)
# # result = re.match(r"[a-zA-Z]+@[a-zA-Z]+[.][a-zA-Z]+", email) # 알파벳만 허용하는 경우
# if result is None:
#     print("잘못된 email 주소입니다.")
# else:
#     print(f"{result.group()} : 올바른 email 주소입니다.")

test = [1]
test[0]