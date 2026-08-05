# re_option.py

import re
p = re.compile("a.b")
print(p.match("a\nb"))   # None, 정규표현식에서 .은 개행문자를 무시함


p = re.compile("a.b", re.DOTALL)
print(p.match("a\nb"))   # "a\nb", \과 n을 각각 별개의 문자로 봄

p = re.compile("a.b", re.S)
print(p.match("a\nb"))   # "a\nb", \과 n을 각각 별개의 문자로 봄

print("-----------------------------")

p = re.compile("[a-z]+", re.IGNORECASE)
# p = re.compile("[a-z]+", re.I)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))

print("-----------------------------")
p = re.compile("^python\s\w+", re.MULTILINE) # \s : 공백, \w : 숫자 or 문자 or _
# p = re.compile("^python\s\w+", re.M)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

print("-----------------------------")
p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);', re.VERBOSE)
# p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);', re.X)
p = re.compile(r"""                # & : 문자 엔티티의 시작을 나타냄(HTML 엔티티)
               &[#]                # 숫자형 엔티티(문자 개체 참조) 시작
                (0[0-7]            # 반드시 0으로 시작 + Octa form(8진수 형식)
                +|[0-9]+           # Decimal form(10진수)
                |x[0-9a-fA-F]+     # 반드시 x로 시작 + Hexadecimal form(16진수)
                );""",             # ; 문자 엔티티의 끝을 나타냄
                  re.X)
data = "&#07; &#08; &#x0A"
