# slicing.py

# 슬라이싱
# 리스트_변수명[시작_인덱스: 끝_인덱스(미포함)]

week = ['월', '화', '수', '목', '금', '토' ,'일']
print(week)
print(week[0:3])
print(week)
print(week[3:7])

# 인덱스 생략이 가능한 경우: 
# 1. 시작 인덱스가 0인 경우, 
print(week[:4])
# 2. 마지막 데이터까지 접근하는 경우
print(week[4:])

# 음수 인덱싱
print(week[-2])
print(week[-1])

# 음수 슬라이싱
print(week[-3:])
print(week[-3:-1])
print(week[:] == week)
print(week[:] is week)

print('///',week[-5 : -2])
print("------------------------")
print(week[2::2])
print(week[-1::-1])
print(week[8::-3])
print(week[:10:1])

print(week[5 : 1 : -1])