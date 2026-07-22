# file_read.py

f = open(r"ch12\file2.txt", 'r', encoding = "utf-8")

data = f.read()
print(data)

f.close()