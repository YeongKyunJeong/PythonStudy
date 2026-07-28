# iterator2.py

# 이터레이터 생성 방법 2
# => 클래스 활용

data = [1, 2, 3]

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        
        result = self.data[self.position]
        self.position += 1

        return result

if __name__ == "__main__":
    # i = MyIterator([1, 2, 3])

    # print(type(i))
    # for item in i:
    #     print(item)

    # print("__next__" in dir(i))
    # print(hasattr(i, "__iter__"))

    i2 = MyIterator([1, 2, 3])

    print(next(i2))
    print(next(i2))

    for item in i2:
        print(item)