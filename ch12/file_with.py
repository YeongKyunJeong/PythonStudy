# file_with.py

path = r"ch12\file2.txt"
mode = "w"

with open(path, mode) as f:
    f.write("No pain, no gain.")