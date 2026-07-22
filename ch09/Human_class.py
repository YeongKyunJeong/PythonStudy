# Human_class.py

# 클래스 : 인간
# 객체 : 사람1, 사람2, ...
# 기능 : 자기 소개하다, 자다, 말하다, 먹다
# 속성 : 이름, 나이

class Human:
    # 1. 멤버 변수
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

    def sleep(self, sleeptime):
        print(f"{sleeptime} 시간 잤습니다.")

    def speak(self, text):
        print(f"{text}")


# 객체 생성
kim = Human(14, "김 카사디안")
kim.introduce()
kim.sleep(32)
lee = Human(52, "킴블 리")
lee.introduce()
lee.eat()
