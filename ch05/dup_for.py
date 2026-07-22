# dup_for.py

# for 변수 in 시퀀스1
#    코드블록1
#    for 변수 in 시퀀스2
#       코드블록2

for i in range(5):
    for j in range(10):
        print("*", end = " ")
    print()

for i in range(5):
    for j in range(10):
        print("(", i, ", ", j, ")", sep = "", end = " ")
    print()