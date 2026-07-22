# assignment.py

# 과일 = ['사과', '귤', '수박']
# for 변수 in 과일:
#     print(변수)

# for var in [10, 20, 30]:
#     print(var)

# 가격리스트 = [100, 200, 300]
# for price in 가격리스트:
#     print(price + 10)

# 리스트 = ['dog', 'cat', 'parrot']
# for animal in 리스트:
#     print(animal, len(animal))

# 리스트 = ["가", "나", "다", "라"]
# for i in range(1, 4):
#     print(리스트[i])

# 리스트 = [3, -20, -3, 44]
# for num in 리스트:
#     if num < 0:
#         print(num)

# for year in range(2002, 2051, 4):
#     print(year)

# num = 0
# sum = 0
# while num < 100:
#     num += 1
#     sum += num
# print(sum)

# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i, ": 짝수")
#     else:
#         print(i, ": 홀수")

# odds = []
# evens = []
# for i in range(1, 31):
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(odds)
# print(evens)

# a = 3.14
# b = True
# c = "False"

# print(type(a), type(b), type(c))

# a = int(input("첫 숫자를 입력하세요."))
# b = int(input("다음 숫자를 입력하세요."))
# print("덧셈: ", a, "+", b, "=", a+b)
# print("뺄셈: ", a, "-", b, "=", a-b)
# print("곱셈: ", a, "×", b, "=", a*b)
# print("나눗셈: ", a, "÷", b, "=", a/b)

# water = 700
# if water >= 1000:
#     print("충분")
# elif water < 1000 and water >= 500:
#     print("적절")
# else:
#     print("부족")

# score = int(input("학점을 입력하세요."))
# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# else:
#     print("F학점")

# fruits = ["banana", "peach", "lemon", "grape"]

# print(fruits[2])

# student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
# student3["도시"] = "수원"
# print(student3.keys())

# Numbers = [1, 2, 3, 4, 5]

# for number in Numbers:
#     print(number)

fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']

for fruit in fruits:
    print(fruit)
    if(fruit == '사과'):
        print("사과를 찾았습니다!")