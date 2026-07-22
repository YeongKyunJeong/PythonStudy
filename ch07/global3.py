# global3.py

def scope_test1():
    a = 1
    a = a + 3
    print("함수 내부 a =", a)

def scope_test2():
    global a
    a = a + 3
    print("함수 내부 a =", a)

a = 0
print("전역 변수 a =", a)
scope_test1()
scope_test2()