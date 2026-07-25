# re1.py

# 정규표현식(Regular Expression)
# : 문자열 패턴을 정의해서
# 검색, 검사, 치환, 추출 등을 수행하는
# 문자열 처리 규칙

# 정규표현식을 정의해서 compile() 함수의 인수로 전달
# -> 패턴 객체로 반환
# 패턴 객체 : "검색대상문자열"에서 패턴 발견을 도와주는 객체

# 메타 문자 : 별도의 의미가 담긴 문자

# [] 문자
# [] 사이에는 대부분의 문자(기호) 포함 가능
# 메타문자도 사용 가능(대무분은 별도의 의미 없음)

# [abc] : a, b, c 중 한 개의 문자와 매치

## 정규표현식 문법
# 패턴_객체명 = re.compile("정규표현식")     # 패턴(규칙) 생성
# 매치_객체 = 패턴_객체.match()
# print(매치_객체)

# match() 함수: "문자열의 처음부터" 정규표현식과 매치되는지 조사함

import re

# p = re.compile("[abc]")
# m1 = p.match("a")
# m2 = p.match("before")
# m3 = p.match("dude")
# print(m1)
# print(m2)
# print(m3)

# p = re.compile("[ab]")    # a or b
# p = re.compile("ab")      # ab

# p1 = re.compile("[a]")

# print(p1.match("apple"))       # 'a'
# print(p1.match("banana"))      # None (처음부터 매치했을 때 a가 매치되지 않으므로)
# print(p1.match("watermelon"))  # None (처음부터 매치했을 때 a가 매치되지 않으므로)

# p2 = re.compile("a")
# print(p2.match("apple"))       # 'a'
# print(p2.match("banana"))      # None (처음부터 매치했을 때 a가 매치되지 않으므로)
# print(p2.match("watermelon"))  # None (처음부터 매치했을 때 a가 매치되지 않으므로)

# p3 = re.compile("[ab]")
# print(p3.match("apple"))       # 'a'
# print(p3.match("banana"))      # 'b'
# print(p3.match("watermelon"))  # None


# p4 = re.compile("[ab]")
# print(p4.match("apple"))       # None
# print(p4.match("banana"))      # None
# print(p4.match("watermelon"))  # None
# print(p4.match("absolute"))    # 'ab'

# p5 = re.compile("[a-c]")
# print(p5.match("apple"))       # a
# print(p5.match("banana"))      # b
# print(p5.match("watermelon"))  # None

# p6 = re.compile("[0-5]")
# print(p6.match("1:apple"))       # 1
# print(p6.match("2:banana"))      # 2
# print(p6.match("7:watermelon"))  # None

# p7 = re.compile("[a-zA-Z]")
# print(p7.match("apple"))       # a
# print(p7.match("banana"))      # b
# print(p7.match("watermelon"))  # w

# pc = re.compile("[^abc]")      # a, b, c 제외
# print(pc.match("apple"))       # None
# print(pc.match("^apple"))      # ^
# print(pc.match("banana"))      # None
# print(pc.match("watermelon"))  # w

# pbs = re.compile("[\^abc]")      # ^, a, b, c
# print(pbs.match("apple"))        # a
# print(pbs.match("^apple"))       # ^
# print(pbs.match("banana"))       # b
# print(pbs.match("watermelon"))   # None

# pex1 = re.compile("\d")            # [0-9]
# print(pex1.match("1:apple"))       # 1
# print(pex1.match("2:banana"))      # 2
# print(pex1.match("7:watermelon"))  # 7

# pex2 = re.compile("\D")            # [^0-9]
# print(pex2.match("1:apple"))       # None
# print(pex2.match("2:banana"))      # None
# print(pex2.match("7:watermelon"))  # None

# ps1 = re.compile("\s")            # [ \t\n\r\f\v]
# print(ps1.match(" apple"))        # ' '
# print(ps1.match("\tbanana"))      # '\t'
# print(ps1.match("\nwatermelon"))  # '\n'

# ps2 = re.compile("\S")            # [^ \t\n\r\f\v]
# print(ps2.match(" apple"))        # None
# print(ps2.match("\tbanana"))      # None
# print(ps2.match("\nwatermelon"))  # None

# pw1 = re.compile("\w")           # [a-zA-Z0-9_]
# print(pw1.match("apple"))        # a
# print(pw1.match("banana"))       # b
# print(pw1.match("melon"))        # m
# print(pw1.match("_orange"))      # _

# pw2 = re.compile("\W")           # [^a-zA-Z0-9_]
# print(pw2.match("apple"))        # None
# print(pw2.match("banana"))       # None
# print(pw2.match("melon"))        # None
# print(pw2.match("_orange"))      # None

# p = re.compile(".")
# print(p.match("apple"))     # a

# p = re.compile("..")
# print(p.match("apple"))      # ap

# p = re.compile("a.b")
# print(p.match("aab"))      # aab
# print(p.match("a0b"))      # a0b
# print(p.match("a.b"))      # a.b  (여기서 .는 단순 문자열)
# print(p.match("a000b"))    # None (a와 b 사이 하나만 들어가야 함)
# print(p.match("abc"))      # None
# print(p.match("a\tb"))     # a\tb (\t는 탭 1개 = 문자)
# print(p.match("a\nb"))     # None (\n는 문자로 취급X)

# p = re.compile("a[.]b")
# print(p.match("aab"))      # None
# print(p.match("a.b"))      # a.b  (여기서 .는 단순 문자열)
# print(p.match("a000b"))    # None 
# print(p.match("abc"))      # None
# print(p.match("a\tb"))     # None
# print(p.match("a\nb"))     # None

# p = re.compile("a*") 
# print(p.match("apple"))      # a
# print(p.match("pple"))       # ''
# print(p.match("aaapple"))    # aaa

# p = re.compile("ca*") 
# print(p.match("ca"))         # ca
# print(p.match("caaaaat"))    # caaaaat
# print(p.match("cat"))        # cat
# print(p.match("pple"))       # None
# print(p.match("aaapple"))    # None

# p = re.compile("a*") 
# print(p.match("apple"))      # a
# print(p.match("pple"))       # ''
# print(p.match("aaapple"))    # aaa

# p = re.compile("ca+t") 
# print(p.match("ct"))         # None
# print(p.match("caat"))       # caat
# print(p.match("caaaaat"))    # caaaaat
# print(p.match("pple"))       # None
# print(p.match("aaapple"))    # None

# p = re.compile("ca{2}t") 
# print(p.match("ct"))         # None
# print(p.match("caat"))       # caat
# print(p.match("caaaaat"))    # None
# print(p.match("caatcaat"))   # caat


# p = re.compile("ca{2,4}t") 
# print(p.match("cat"))        # None
# print(p.match("caat"))       # caat
# print(p.match("caaat"))      # caaat
# print(p.match("caaaat"))     # caaaat
# print(p.match("caaaaat"))    # None

# p = re.compile("ca{2,}t") 
# print(p.match("cat"))        # None
# print(p.match("caat"))       # caat
# print(p.match("caaat"))      # caaat

# p = re.compile("ca{,1}t") 
# print(p.match("ct"))        # ct
# print(p.match("cat"))       # cat
# print(p.match("caat"))      # None

# p = re.compile("ca?t")
# print(p.match("ct"))          # ca
# print(p.match("cat"))         # cat 
# print(p.match("caat"))        # None

# p = re.compile("[^hello]")     # not
# p = re.compile("^hello")         
# print(p.match("hello world!"))    # hello
# print(p.match(" hello world!"))   # None
# print(p.match("\nhello world!"))  # None
# print(p.match("pello world!"))    # None

p = re.compile("world$")           
print(p.match("world"))             # world
print(p.match("hello world!"))      # None
print(p.match("hello world "))      # None
print(p.match("hello world\n"))     # None
print(p.match("hello world"))       # None 
                                    # <= match가 앞에서부터 일치하는 것을 찾는 함수
                                    # => 앞에서부터도 world, 뒤에서부터도 wolrd여야 매치
print(p.match("world hello world")) # None 
# match()는 문자열의 처음부터 패턴을 찾음
# "world$"는 문자열의 끝에 world의 유무 검색
print(p.search("world hello world")) # world
print("----------------------")
print(p.search("world hello world"))   # world
print(p.search("world hello world!"))  # None
print(p.search("world hello world\n")) # world

p = re.compile("^hello world$")  

print("----------------")
p = re.compile("^hello world$")  
print(p.search("hello world\n")) # hello world
print(p.search("hello python world\n")) # None