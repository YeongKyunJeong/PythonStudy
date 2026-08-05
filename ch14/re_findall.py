# re_findall.py
import re

text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. "
p = re.compile("[Pp]ython")
m = p.findall(text)
print(m)
print(len(m))

print("-------------------")
p = re.compile('[a-z]+')
m = p.findall("life is too short")
print(m)
m = p.findall("life\nis\ttoo8short")
print(m)
