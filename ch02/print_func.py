# print_func.py

na = 10
sa = "python"

print(na)
print(sa)

print(na, sa)

na = 10
nb = 20.2
sa = "python"
print("na변수값", na)
print("nb변수값", nb)
print("sa변수", sa)

nc = 30
nd = 40
print("nc=", nc, "nd=", nd, end = "\n\n")
nd = nc
ne = 30
print("nc=", nc, "nd=", nd)
print(id(nc), "\n", id(nd), "\n" ,id(ne), sep = "")