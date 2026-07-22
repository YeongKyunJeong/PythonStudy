# list2.py

# 값 추가하기
# 리스트_변수명.append(추가할_값)

# listc = []      # 빈 리스트
# print(type(listc))
# print(listc)
# listc.append(300)
# print(listc)
# listc.append('파이썬')
# listc.append(True)
# listc.append('300')
# listc.append([1.1, 3, True])
# print(listc)
# print(listc[4][1])

listd = []
x = 3
listd.append(x if x > 5 else 0)
print(listd)
listd.append(x > 5)
print(listd)
