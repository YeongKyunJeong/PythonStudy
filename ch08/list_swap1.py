# list_swap1.py

# ca = [10, 11]
# ca[0], ca[1] = ca[1], ca[0]
# print(ca)

# print("----------------------")
# def funca(na, nb):
#     na, nb = nb, na

# def funcb(cb):
#     cb[0], cb[1] = cb[1], cb[0]

# ca = [10, 11]
# funca(ca[0], ca[1])
# print(ca)
# funcb(ca)
# print(ca)

print("----------------------")

ca = [10, 11]
cb = ca
print("ca =", ca)
print("ca의 주소 :", id(ca))
print("ca[0]의 주소 :", id(ca[0]))
print("ca[1]의 주소 :", id(ca[1]))
print("cb =", cb)
print("cb의 주소 =", id(cb))
print("cb[0]의 주소 :", id(cb[0]))
print("cb[1]의 주소 :", id(cb[1]))

print("----------------------")

temp = cb[0]
cb[0] = cb[1]
cb[1] = temp

print("ca =", ca)
print("cb =", cb)

