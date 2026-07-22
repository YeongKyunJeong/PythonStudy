# swap2.py

def swap1():
    global na, nb
    temp = na
    na = nb
    nb = temp
    
na = 10
nb = 11
print("na:", na, "nb:", nb)
swap1()
print("na:", na, "nb:", nb)

# def swap2(pa, pb):
#     temp = pa
#     pa = pb
#     pb = temp
#     return pa, pb

# na, nb = swap2(na, nb)
# print("na:", na, "nb:", nb)