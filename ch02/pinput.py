# pinput.py

print("첫 번째 정수를 입력하세요") # 20을 입력
ra = input() # ①
rb = input("두 번째 정수를 입력하세요\n") # 5를 입력 ②
print(type(ra))
print(type(rb))
ra = int(ra)
rb = int(rb)
rc = ra + rb # ③
print(ra, "+", rb, "=", rc)
