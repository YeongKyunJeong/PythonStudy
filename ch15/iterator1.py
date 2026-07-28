# iterator1.py

# 이터레이터 생성 방법 1
# => iter() 함수 사용

data = [1, 2, 3]
iterator = iter(data)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))     # StopIteration

# __iter__() 메서드의 구현 여부 확인법
print("__iter__" in dir(data))
print(hasattr(iterator, "__iter__"))
print("__next__" in dir(data))
print(hasattr(data, "__next__"))