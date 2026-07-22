# file_append.py

path = r"ch12\file2.txt"
f = open(path, 'a', 
         encoding = "utf-8")

for i in range(11, 21): # 11 ~ 20
    data = "%d번째 줄입니다.\n" %i
    f.write(data)

f.close()