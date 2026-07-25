# re_search.py

import re

p = re.compile("[a-z]+")
# m = p.search("python")
m = p.search("3 python")
print(m)

print("-----------------")
if m:
    print(f"Match found : {m.group()}")
    print(f"Start : {m.start()}")
    print(f"End : {m.end()}")
    print(f"Span : {m.span()}")
else:
    print("No match")

print("--------------")
