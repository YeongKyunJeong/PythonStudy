# func1.py

# 함수 정의
# def 함수명(매개변수):
#   코드블록
#   return 반환값

# 함수 호출
# 변수 = 함수명([인수])

# def my_func():
#     print("토끼야 안녕!")
#     print("거북아 안녕")
#     return

# my_func()

# # 함수 정의
# def func1(pa, pb):
#     print("hi")
#     print(pa, pb)
#     print(type(pa), type(pb))

# # 함수 호출
# # pa = 3
# # pb = 9
# func1(3, "9")

# def fhello():
#     print("매개변수 없는 함수 호출하기")

# fhello()

# def funca(na, nb):
#     nc = na + nb
#     print(na, "+", nb, "=", nc)

# funca(10, 20)

# funca("hi", "my")

# def add(num1, num2):
#     # sum = num1 + num2
#     return num1 + num2

# # result = add(2, 3)
# print(add(2, 3))

# def sub(num1, num2):
#     diff = num1 - num2
#     return diff

# print(sub(120, 49))

# def pr1(end):
    # sum = 0
#     diff = 1 if end >= 1 else -1
#     for num in range(1, end + diff , diff):
#         sum += num

#     print("result =", sum)

#     return sum

# def pr1_1(end):
#     now = 1
#     sum = 1
#     if end >= 1:
#         diff = 1
#         while now < end:
#             now += diff
#             sum += now

#     else : 
#         diff = -1
#         while now > end:
#             now += diff
#             sum += now

#     return sum

# num = int(input("정수를 입력하세요"))
# print(pr1(num))
# print(pr1_1(num))
