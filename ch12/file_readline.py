# file_read.py

f = open(r"ch12\file2.txt", 'r', encoding = "utf-8")

for i in range(1, 11):
    line = f.readline()
    print(line, end = "")

f.close()