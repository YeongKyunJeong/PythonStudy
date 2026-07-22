# Cexm_calss.py

# class 클래스명:
#     1. 멤버변수
#     변수명 = 데이터값
#     # 2. 메서드
#     # def 함수명(self, 매개변수):
#           코드블록
#           self.변수명 = 데이터값
#           return 반환값

class Cexm:

    def fsam(self):
        print("멤버 함수(메서드)")

    def fsbm(self, pa):
        self.x = pa
        print("멤버 변수 x는", self.x)

ca = Cexm()
ca.fsam()
ca.fsbm(10)

cb = Cexm()
cb.fsbm(20)