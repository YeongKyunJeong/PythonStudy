# pizza_class.py

# class 클래스명:
#     멤버 변수 = 데이터 값
#     코드블록
#     def 메서드명(self, 매개변수)
#         self.멤버변수명2 = 데이터값
#         return 반환값

class PizzaClass:
    
    def __init__(self, m):
        print("피자", self, m)
        self.m = m + 20
        print(self.m, m)


    def order(self):
        print("주문")
        self.kind = 10
        return 

pizza1 = PizzaClass(3)

# 객체변수명.멤버함수명(인수)
# order에서 self 이후의 파라미터에 인수가 전달됨
pizza1.order()
# 객체변수명.멤버변수명
print(pizza1.kind)

# 변수명 = 클래스명(인수)
