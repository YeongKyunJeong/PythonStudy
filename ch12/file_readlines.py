# file_readlines.py

f = open(r"ch12\file2.txt", 'r', encoding = "utf-8")

lines = f.readlines()
for line in lines:
    print(line, end = "")

f.close()