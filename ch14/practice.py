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
# print(numbers)

# text = "I love Python. Java is also popular. Python is great for AI."
# import re
# sentence = re.findall(r"[\w\s]+[.]", text)
# print(sentence)

# text = "상품 코드: A123, B456, C789, 가격: 12000원"
# import re
# prices = re.findall( r"\d+", text)
# print(prices)

text = "NASA is working on AI projects with IBM and Google."
import re
uppers = re.findall(r"[A-Z]{2,}", text)
print(uppers)
