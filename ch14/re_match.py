# re_match.py

# p = re.compile(메타문자를 활용한 정규표현식)
# m = p.match(패턴 일치 여부를 확인할 문자열)

# p : 컴파일된 패턴 객체

import re
p = re.compile('[a-z]+')
m = p.match("python")       # 'python'
# print(m)
# m = p.match("3 python")     # None
# print(m)

# p = re.compile('[a-z0-9]+')
# m = p.match("a12")     # None
# print(m)

if m: # match 객체가 있을 때 => True
    print(f"Match found: {m.group()}")
    print(f"Start: {m.start()}")
    print(f"End: {m.end()}")
    print(f"Span: {m.span()}")