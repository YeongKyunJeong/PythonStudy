# default3.py

def person_c(height = 162, weight = 54, age = 21):
    print("height = ", height, end = ", ")
    print("weight = ", weight, end = ", ")
    print("age = ", age)

# 위치 인수: 순서대로 전달하는 인수
person_c(177, 55)

# 키워드 인수: 매개변수 이름을 지정해 전달하는 인수
person_c(weight= 45)

# 위치 인수 + 키워드 인수
person_c(178, weight= 45)
