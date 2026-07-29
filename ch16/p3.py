# p3.py

# 문제 1. 은행 번호표 시스템

from queue_class import Queue

from queue_class import Queue
# 번호표 => 1: 철수, 2: 영희, 3: 민수
waits = {1: "철수", 2: "영희", 3: "민수"}

bank = Queue()
for wait in waits:
    bank.enqueue(waits[wait])
    print(bank.status_queue())

while not bank.is_empty():
    print(f"{bank.dequeue()}의 업무 처리")

# 문제 2. 브라우저 뒤로가기 시스템

from stack_class import Stack

visited = Stack()

visited.push("a")
visited.push("b")
visited.push("c")
visited.push("d")

print(visited.status_stack())

while not visited.is_empty():
    print(f"현재 페이지 : {visited.peak()}")
    visited.pop()


print(visited.status_stack())

