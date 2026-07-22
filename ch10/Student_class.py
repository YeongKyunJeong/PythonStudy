# Student_class.py

# 클래스 : 인간
# 객체 : 사람1, 사람2, ...
# 기능 : 자기 소개하다, 자다, 말하다, 먹다
# 속성 : 이름, 나이

class Human:
    # 1. 멤버 변수
    eyes = 2
    nose = 1
    mouth = 1

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.stomach = []

    # 2. 메서드
    def introduce(self):
        print(self.age, "살", end = " ")
        print(self.name, "입니다.", sep = "")

    def eat(self, food = ''):
        if len(food) == 0:
            print("먹은 게 없습니다.")
            return
        self.stomach.append(food)
        print(f"지금까지 먹은 음식 : {self.stomach}")

    def sleep(self, sleeptime):
        print(f"{sleeptime} 시간 잤습니다.")

    def speak(self, text):
        print(f"{text}")

print(f"눈의 개수: {Human.eyes}")
lee = Human(49, "이수근")
lee.introduce()
lee.eat("밥")

class Student(Human):

    def __init__(self, age, name, studentnNum):    # 새로 정의된 함수가 우선순위가 높음
        super().__init__(age, name)                # 부모 클래스에 있는 __init__() 메서드
        self.studentNum = studentnNum

    def study(self):
        print("공부하다")

    def introduce(self):
        print(self.studentNum, "학번", end = " ")
        super().introduce()

print("---------------------")
high = Student(24, "최하이", 20260720)
# high = Student()
high.study()
print(high.mouth)
high.sleep(50)
high.introduce()