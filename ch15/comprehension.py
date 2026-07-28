# comprehension.py

# 1. 리스트 컴프리핸션 : 새 리스트 생성
# [expression for item in iterable if condition]
# expression : 새 리스트 각 요소 정의
# item : 이터러블의 각 요소
# iterable : 반복 가능한 객체 (리스트, 튜플, 문자열 등)
# condition : 조건문이 참인 경우에만 요소에 포함

# numbers = [1, 2, 3, 4]
# print( [x**2 for x in numbers])

# numbers = [1, 2, 3, 4]
# print( [x for x in numbers if x % 2 == 0])

# squared_plus = [x**2 + 1 for x in numbers if x % 2 == 0]
# print(squared_plus)

# 2. 딕셔너리 컴프리핸션 : 새 딕셔너리 생성
# {key_expression : value_expression for item in iterable if condition}
# key_expression : 새 딕셔너리 key 요소 정의
# value_expression : 새 딕셔너리 value 요소 정의
# item : 이터러블의 각 요소
# iterable : 반복 가능한 객체 (리스트, 튜플, 문자열 등)
# condition : 조건문이 참인 경우에만 요소에 포함

print("----------------------")
print({x : x**2 for x in range(5)})
print({x : x**2 for x in range(5) if x % 2 == 0})

subjects = ['수학', '영어', '역사']
scores = [90 , 78, 81]
scores = {subject : score for subject, score in zip(subjects, scores)}
print(scores)

for subject, score in scores.items():
    print(f"{subject} : {score}")

grade  = {
    subject : "합격" if score >= 60 else '불합격'
    for subject, score in scores.items()
}
print(grade)


print("----------------------")

# 3. 제너레이터 컴프리핸션 : 새 제너레이터 생성
# (expression for item in iterable if condition)
# expression : 새 제너레이터 각 요소 정의
# item : 이터러블의 각 요소
# iterable : 반복 가능한 객체 (리스트, 튜플, 문자열 등)
# condition : 조건문이 참인 경우에만 요소에 포함
gen = (i*i for i in range(1, 10))
print(type(gen))
print(gen.__next__())
print(next(gen))

