# p2.py

from collections import deque

def rotate_queue(queue, k):
    dq = deque(queue)

    for _ in  range(k):
        dq.append(dq.popleft())

    return list(dq)

queue = [1, 2, 3, 4, 5]
k = 2
print(rotate_queue(queue, k))

dq = deque(queue)
dq.rotate(-2)