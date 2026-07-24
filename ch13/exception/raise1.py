# raise1.py

# raise 예외클래스명(예외_정보_데이터)

# print("raise")
# raise NameError('Hi There')   # 예외 발생
# print('exit')

# print("raise")
# try:
#     raise ValueError('Hi There')   # 예외 발생
# except NameError as e:
#     print('An exception flew by!')
#     print(e)
# except ValueError as e:
#     print('An exception flew by!')
#     print(e)
# print('exit')

class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError
        self.balance -= amount
        return self.balance

lim = Account(1000)
print(lim.withdraw(2000))