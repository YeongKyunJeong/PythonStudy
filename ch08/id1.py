# id1.py

a = [10, 11, 12, 13]
print("list a 값:", a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))

a[1] = 21 
print("list a 값:", a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))

b = a                     # b에 a 할당
print("list b 값:", b)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))

b = [30, 31, 32, 33]      # b 값에 재할당
print("list b 값:", b)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))

def fk(cb):
    total = 0
    for sb in range(0, 3, 1):
        total += cb[sb]
    cb[2] = total
    
    return cb

ca = [10, 20, 30]
print(ca)
cd = fk(ca)
print(ca)
print(cd)
