# assignment.py

# try:
#     x = int("abc")
# except (ValueError, TypeError):
#     print("ValueError occurred!")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# finally:
#     print("Execution finished.")

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     raise(KeyError)
# except KeyError:
#     print("Key is missing!")

# add = lambda x, y : x + y
# print(add(3, 5))

# per = ["10.31", "", "8.00"]
# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         print(0)

numbers = [10, 20, 30]
idx = input("인덱스를 입력하세요.")
try:
    idx = int(idx)
    print(numbers[idx])
except IndexError:
    print("잘못된 인덱스입니다.")
except ValueError:
    print("숫자를 입력해주세요.")
