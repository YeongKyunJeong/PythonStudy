# list_remove.py

# 값 제거하기
# 리스트_변수명.remove(제거할_값)

subjects = ['국어', '수학', '영어', '국사']
print(subjects[2])
subjects.remove('영어')
print(subjects)
print(subjects[2])
# print(subjects[3])      # indexError

print("------------------------")
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
del clovers[1]
print(clovers)
print(clovers[1])
