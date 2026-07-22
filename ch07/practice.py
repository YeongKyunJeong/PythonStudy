# practice.py

# x = 10
# def fadd(num):
#     b = x + num            # b가 정의된 적이 없는데 b = b + x + num 시도
#     print("변수 x의 값은", x)
#     print("변수 b의 값은", b)
# fadd(10)

# x = 7
# def fadd(num):
#     x = x + num               # 내부 변수 x에 r_value가 할당된 적이 없는데 'x + num'에서 호출 시도
#     print("변수 x의 값은", x)
# fadd(10)

# x = 7
# def fadd(num):
#     x = num
#     print("변수 x의 값은", x)
# fadd(10)

# x = 10
# def fadd(num):
#     global x
#     x += x + num
#     print("변수 x의 값은", x)
# print(fadd(10))

# def print_lower_price(cur_price):
#     return print(0.9*cur_price)
  
# print_lower_price(14510000)

# def func1(num):
#     return num + 4

# a = func1(10)
# b = func1(a)
# c = func1(b)
# print(c)

# x = 7
# def fadd(num):
#     b = x + num
#     x = 17
#     print(b)
# fadd(10)

x = 7
def fadd(num):
    x = 17
    b = x + num
    print(b)
fadd(10)
