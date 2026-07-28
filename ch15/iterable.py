# iterable.py

# 1. iterable : 반복 가능한
# 2. iterator : 반복자

a = [1, 2, 3]
# next(a)         # 값을 순차적으로 반환
iter_a = iter(a)
# print(next(a_iter))
# print(type(a_iter))

for j in iter_a:
    print(j)

iter_a = iter([1, 2, 3])
for i in iter_a:
    continue
print(next(iter_a))        #