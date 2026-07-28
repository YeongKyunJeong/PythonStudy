# assignment.py

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# gen = countdown(3)
# for x in gen:
#     print(x, end=" ")

# numbers = [1, 2, 3, 4, 5]
# for num in numbers.__iter__():
#     print(num)

# class MyIter:
#     def __init__(self, data):
#         self.data = data
#         self.position = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.position >= len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position += 1
#         return result

# for num in MyIter(numbers):
#     print(num)

# for num in (number for number in numbers):
#     print(num)

# fruits = ["apple", "banana", "cherry"]
# iter_fruits = fruits.__iter__()
# while True:
#     try:
#         print(iter_fruits.__next__())
#     except StopIteration:
#         break

# for squared_x in (x*x for x in range(0, 10)):
#     print(squared_x)

# gen = (x*x for x in range(0, 10))
# for squared_x in gen:
#     print(squared_x)

# iter_a = (x for x in range(0, 11) if x % 2 == 0)
# for even in iter_a:
#     print(even)

class MyRange:
    def __init__(self, start, end, step):
        if step == 0:
            raise ValueError("step은 0일 수 없습니다.")
        self.now = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.step > 0 and self.now >= self.end:
            raise StopIteration
        elif self.step < 0 and self.now <= self.end:
            raise StopIteration
        result = self.now
        self.now += self.step
        return result



for i in range(1, 6, 2):
    print(i)

for i in MyRange(1, 6, 2):
    print(i)