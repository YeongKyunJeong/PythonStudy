# tuple1.py

# tuple 생성 방법
# clovers = ('클로버1', '하트2', '클로버3')
# print(clovers)
# print(type(clovers))

# # tuple 접근 방법
# print(clovers[0])
# print(clovers[1])
# print(clovers[2])

# print('------------------------')
# my_tuple1 = () 
# print(my_tuple1)
# print(type(my_tuple1))
# my_tuple1 = (True, 1, "튜플")
# print(my_tuple1[0])
# print(my_tuple1[1])
# print(my_tuple1[2])

# print('------------------------')
# my_tuple2 = (1, -2, 3.14, True, "hi")
# print(my_tuple2)

# my_tuple3 = 1, -2, 3.14, True, "hi"
# print(my_tuple3)

# my_tuple4 = ("hi")
# print(my_tuple4)
# print(type(my_tuple4))

# my_tuple5 = ("hi",)
# print(my_tuple5)
# print(type(my_tuple5))
# print("----------------------")
a = (1, 2, 3)
# a[0] = 7

print(a, "a의 데이터 형식은", type(a))
b = list(a)
print(b, "b의 형식은", type(b))
b[0] = 7
print(b)
a = tuple(b)
print(a)
