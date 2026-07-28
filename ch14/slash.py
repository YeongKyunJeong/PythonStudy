# slash.py
## 역슬래시 문제

import re

# 패턴객체 = re.compile("정규표현식")
# 매치객체 = 패턴객체.match("대상문자열")

# p = re.compile("\\\\section")
# m = p.match("\\section python hello thanks")

p = re.compile("\\\\new")
m = p.match("\new python hello thanks")

print(m)