# Singer_class.py

# 클래스 정의
class Singer:
    # 속성(멤버 변수)
    iu_name = "아이유"
    bts_name = "BTS"

    # 기능/동작(메서드)
    def sing_iu(self):
        print("이 밤 그날의 반딧불을 당신의 창~")

    def sing_bts(self):
        print("~~~~")

# print(Singer.iu_name)
# print(Singer.bts_name)

# 객체 생성(사용)
iu = Singer()
# print(iu.iu_name)
# iu.sing_iu()

bts = Singer()
# print(iu.bts_name)
# bts.sing_bts()

bts.bts_name = "비티에스"
print(iu.bts_name)
print(bts.bts_name)

Singer.bts_name = "비티에스2"
print(iu.bts_name)
print(bts.bts_name)

