# file_open.py

# 현재 디렉터라: C:\ROKEY\py_work
# 파일 열기
# f = open("./ch12/file1.txt", "w")     # 상대경로
f = open("C:/ROKEY/py_work/ch12/file1.txt", "w")
f = open(r"C:\ROKEY\py_work\ch12\file1.txt", "w")
# 파일 닫기
f.close()

# 인코딩 : 문자를 숫자화
print(ord("A"))
print(ord("a"))
print(ord("가"))

# 디코딩 : 숫자를 문자화
print(chr(65))
print(chr(97))
print(chr(44032))