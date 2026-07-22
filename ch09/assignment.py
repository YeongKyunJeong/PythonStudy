# assignment.py

# class Phone():
#     def __init__(self, 제조사, 출고년도, 색상):
#         print("휴대폰 생성")
#         self.제조사 = 제조사
#         self.출고년도 = 출고년도
#         self.색상 = 색상
#     def info(self):
#         print(self.제조사)
#         print(self.출고년도)
#         print(self.색상)
#     def setInfo(self, 제조사, 출고년도, 색상):
#         self.제조사 = 제조사
#         self.출고년도 = 출고년도
#         self.색상 = 색상

# my_phone = Phone("Balam", 2755, "Red")

# my_phone.info()

# my_phone.setInfo("Arcabus", 2760, "Blue")

# my_phone.info()

# def solution(a, b):
#     sum = a + b
#     sub = a - b
#     multi = a * b
#     return sum, sub, multi

# print(solution(10, 5))

# def summation(n):
#     sum = 0
#     for num in range(1,n + 1):
#         sum += num
#     return sum

# print(summation(20))

# x = 10

# def example1():
#     x = 20
#     print(x)

# example1()
# print(x)

# def list_max(num_list):
#     max = num_list[0]       # max 변수 초기화 부분 추가
#     for num in num_list:
#         if max < num:
#             max = num
#     print(max)

# list_max([10, 158, 324 ,81, 3, 85,43])

# def list_min(num_list):
#     min = num_list[0]
#     for num in num_list:
#         if min > num:
#             min = num
#     print(min)

# list_min([10, 158, 324 ,81, 3, 85, 43])

class Student:
    school = "High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Alice", 1)

print(Student.school)
print(s1.school)
print(s1.name)

