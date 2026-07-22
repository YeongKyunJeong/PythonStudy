# practice.py

# def add_item(item, box = []):
#     box.append(item)
#     return box

# print(add_item("a"))
# print(add_item("b"))

# nums = [1, 2, 2, 4]
# for n in nums:
#     if n % 2 == 0:
#         nums.remove(n)

# print(nums)

# print([11, 56, 89] + [4])

# import random
# clovers = ["클로버1", "클로버2", "클로버3"]
# print(random.sample(clovers, 2))

class Car:

    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

# car = Car(4, 3000)
# print(car.wheel)
# print(car.price)

class Bicycle(Car):

    def __init__(self, year, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.year = year
        self.drivetrain = drivetrain

    def info(self):
        print(f"year : {self.year}")
        print(f"wheel : {self.wheel}")
        print(f"price : {self.price}")
        print(f"drivetrain : {self.drivetrain}")

bicycle = Bicycle(2021, 2, 100, "시마노")
# print(bicycle.year)
# print(bicycle.wheel)
# print(bicycle.price)
# print(bicycle.drivetrain)
bicycle.info()