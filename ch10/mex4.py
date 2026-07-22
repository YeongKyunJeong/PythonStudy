# mex4.py

# print("mex4.py")
print(__name__)
# print(type(__name__))

# from 모듈명 import *
# from mex1 import *
from mex5 import *

print("--------------------")
p4 = Cvalue()
p4.add(10)

print(plus(7, 9))
# print(p1.lista)
print(p5.lista)      # mex5.py에서 if __name__ == "__main__"이하 코드가 실행되지 않으므로
                     # 에러 발생