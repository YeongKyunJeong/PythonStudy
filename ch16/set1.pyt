# set1.py

# 세트 생성 (중복 제거)
numbers = {1, 2, 3, 3, 4}
print(numbers)

# 요소 추가 및 제거
numbers.add(5)
numbers.remove(3)
print(numbers)


set1 = {1, 2, 3}
set2 = {3, 4 ,5}

# 교집합
print(set1 & set2) # {3}
# 합집합
print(set1 | set2) # {1, 2, 3, 4, 5}
# 차집합
print(set1 - set2) # {1, 2}

# 산술 연산을 지원하지 않음

print("-"*10)
print([1, 2] + [3, 4])   # [1, 2, 3, 4]
# print({1, 2} + {3, 4})   # TypeError
print({1, 2} | {3, 4})
