# assignment.py

score = int(input("학점을 입력하세요."))

print("grade is ", end = "")
if 100 >= score >= 81:
    print("A")
elif 80 >= score >= 61:
    print("B")
elif 60 >= score >= 41:
    print("C")
elif 40 >= score >= 21:
    print("D")
elif 20 >= score >= 0:
    print("E")