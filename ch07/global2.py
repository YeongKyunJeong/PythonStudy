# global1.py

def scope_test():
    global a
    a = 1      # 전역 변수, 재할당
    # global a   # 함수 내부에서 a의 사용보다 아래에서 선언하면 이미 지역 변수 a가 할당되어 있으므로 에러가 남
    print("함수 내부 a =", a)

a = 0
scope_test()
print("전역 변수 a =", a)