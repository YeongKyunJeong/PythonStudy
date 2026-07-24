# try_except1.py

# 예외 처리 문법
# try:
#     코드블록 - 예외 발생 가능성이 있는 코드
# except 예외클래스:
#     코드블록 - 해당 예외클래스로 발생한 예외 처리
# finally:
#     코드블록 - 예외 처리 후 실행할 명령

# 예)
# try:
#     코드블록 - 예외 발생 가능성이 있는 코드
#     명령어1 -> 실행 완료
#     명령어2 -> 예외 발생
#     명령어3 -> 건너뜀
# except TypeError:
#     코드블록 - 해당 예외클래스로 발생한 예외 처리
# except NameError:
#     코드블록 - 해당 예외클래스로 발생한 예외 처리
# finally:
#     코드블록 - 예외 처리 후 실행할 명령

try:
    # 2 + "2"
    2 + 2
except NameError:
    print("NameError")
finally:
    print("Finally")
print("program end")

# try:
#     3 + spam
# except NameError:
#     print("NameError")
# finally:
#     print("Exception occurs")
# print("program end")