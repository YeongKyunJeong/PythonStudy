
muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))

try:
    muna[0] = 'k'
except TypeError as e:
    print(type(e), e)

munb = ["python"]
print(munb[0])
print(type(munb))

print("------------------")
munc = ["p", "y", "t", "h", "o", "n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0] = 'k'
print(munc)

print("------------------")
for i in range(0, 6, 1):
    print(munc[i], end="")

print("------------------")
length = len(munc)
print(length)

for i in range(0, len(munc)):
    print(munc[i], end="")