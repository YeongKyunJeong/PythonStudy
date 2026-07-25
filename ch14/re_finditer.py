# re_finditer.py

import re
text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. "
p = re.compile("[Pp]ython")
result = p.finditer(text)

for r in result:
    print(f"{r.group()} : {r.span()}")

print("-------------------")
p = re.compile('[a-z]+')
result = p.finditer("life is too short")
for r in result:
    print(f"{r.group()} : {r.span()}")