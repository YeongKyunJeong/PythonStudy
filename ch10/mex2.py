# mex2.py

import mex1
print(type(mex1))

def mul(a, b):
    return a * b

# mex1의 Cvalue 클래스 활용
p2 = mex1.Cvalue()
print(p2.lista)
p2.add(11)
p2.fprint()

print("-------------------")
# mex1의 plus 함수 활용
value = mex1.plus(10, 20)

print("-------------------")
# mex1의 p1 변수 활용
print(mex1.p1.lista)
mex1.p1.add(4)
mex1.p1.fprint()