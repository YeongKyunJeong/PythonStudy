# re_compile.py

# 축약 전 상태
# p = re.compile(정규식표현)
# m = p.match(검색대상문자열)

import re
m = re.match('[a-z]+', "python")
print(m)

print(m.group())
print(m.span())
print(m.start())
print(m.end())