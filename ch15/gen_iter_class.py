# gen_iter.class.py

# 제너레이터와 동일한 이터레이터 클래스 생성
# gen = (i*i for i in range(1, 10))

class MyIterator:
    def __init__(self):
        self.data = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.data >= 10:
            raise StopIteration
        result = self.data * self.data
        self.data += 1
        return result
        
my_iter = MyIterator()
print(type(my_iter))
for i in my_iter:
    print(i)

print(next(my_iter))
print(next(my_iter))