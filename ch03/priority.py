# priority.py

# 연산자 우선순위
# 괄호 > 산술 > 비교 > 논리 > 대입
# 산술: ** > 부호 > *,/,//,% > +,-
# 논리 : not > and > or

print(2 * (3 - 5)) 

print("--------------------")

print(9 > 4 and 3 > 2)
print(9 < 4 and 3 > 2)
print(9 < 4 or 3 < 2)
print(9 < 4 or 3 > 2)

print("--------------------")
print(True or False and False)
print((True or False) and False)

print(4>2 and 9<4 or 3>2)
print((3-5)+3 < 1 and 3-5 > 1)