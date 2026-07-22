# Bag_class.py

# 클래스: 가방
# 객체: 손가방, 책가방, 핸드백, 숄더백
# 속성: 재질, 무게, 크기, 가격 => 변수
# 기능: 닫다, 빼다 => 메서드

# 빈 클래스
class Bag:
    # 1. 멤버 변수(속성, 명사)
    call_name = "가방" # 클래스 멤버 변수
    kind = 0

    # 2. 메서드(기능/동작, 동사)
    def __init__(self, name):           # 초기화 함수
        self.data = []
        kind += 1
        print(name)

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def remove(self, x):
        if isinstance(x, int):
            del self.data[int]
        else:
            self.data.remove(x)

print(Bag.kind)

handbag = Bag("손가방")

handbag.add("스마트폰")
handbag.add("손수건")
handbag.add("거울")
print(handbag.data)

schoolbag = Bag("책가방")
schoolbag.add("교과서")
schoolbag.add("필기구")
schoolbag.add("노트북")
schoolbag.add("충전기")
schoolbag.remove("교과서")
print(schoolbag.data)

print(Bag.kind)
