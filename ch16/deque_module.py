# deque_module.py

from collections import deque

dq = deque()
print(type(dq))

dq.append(1)      # 뒤로 삽입
print(dq)
dq.appendleft(2)  # 앞으로 삽입
print(dq)
dq.appendleft(3)
dq.append(4)
dq.pop()          # 마지막 데이터 제거
print(dq)
dq.popleft()      # 처음 데이터 제거
print(dq)
print(len(dq))

if not dq: # len(dq) == 0
    dq.pop()

dq2 = deque([1, 2, 3, 4]) # 초기값 설정
print(dq2)

# 우측 회전(1)
dq2.rotate(1)
print(dq2)
# 좌측 회전(-1)
dq2.rotate(-1)
print(dq2)
