# try_except2.py

while True:
    try:
        print("명령어1")
        x = int(input("Please, enter a number: "))
        2 + "2"                 # TypeError
        break                   # 실행 안 됨
    except (TypeError, ValueError) as e:
        print("TypeError와 ValueError 처리")
        print(e)
        print(type(e))
    finally:
        print("Try except 구문 종료")
print("프로그램 종료")