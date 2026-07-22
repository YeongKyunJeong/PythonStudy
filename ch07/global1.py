# global1.py

b = 0
print("b =", b)
b = 1
print("b =", b)

def scope_test():
    a = 1
    print("함수 내부 a =", a)

a = 0
print("전역 변수 a =", a)
scope_test()