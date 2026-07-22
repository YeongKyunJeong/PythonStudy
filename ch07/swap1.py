# swap1.py

# 1) 변수간 데이터 SWAP 1
na = 10
nb = 11
temp = na
na = nb
nb = temp
print("na:", na, "nb:", nb)

print("-------------------")

# 2) 변수간 데이터 SWAP 2
na = 10
nb = 11
na, nb = nb, na
print("na:", na, "nb:", nb)

print("-------------------")

def swap1(pa, pb):
    temp = pa
    pa = pb
    pb = temp

na = 10
nb = 11
swap1(na, nb)
print("na:", na, "nb:", nb)

# def swap2(pa, pb):
#     temp = pa
#     pa = pb
#     pb = temp
#     return pa, pb

# na, nb = swap2(na, nb)
# print("na:", na, "nb:", nb)