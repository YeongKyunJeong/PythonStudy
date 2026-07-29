# assignment.py

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def pop(self):
#         if self.is_empty( ):
#             return -1
#         return self.stack.pop()
#     def push(self, data):
#         self.stack.append(data)
#     def top(self):
#         if self.is_empty( ):
#             return -1    
#         return self.stack[-1]
#     def is_empty(self):
#         return len(self.stack) == 0


# st = Stack()
# print(st.pop())
# st.push(1)
# st.push(2)
# st.push(3)
# print(st.stack)
# st.pop()
# print(st.stack)
# print("-"*10)
# print(st.is_empty())
# print(st.top())
# print(st.stack)
# print(st.pop())
# print(st.stack)

# from collections import deque
# def solve(expression):
#     splited = expression.split()
#     operators = {'+', '-', '*', '/'}
#     dq = deque()
#     for chr in splited:
#         if chr in operators:
#             if len(dq) < 2:
#                 raise ValueError("잘못된 수식")
#             right = dq.pop()
#             left = dq.pop()
#             if chr == '+':
#                 dq.append(left + right)
#             if chr == '-':
#                 dq.append(left - right)
#             if chr == '*':
#                 dq.append(left * right)
#             if chr == '/':
#                 dq.append(left / right)
#         else:
#             dq.append(float(chr))
#     if len(dq) > 1 :
#         raise ValueError("잘못된 수식")
#     return dq.pop()

# print(solve('3 4 +'))
# print(solve('6 7 *'))
# print(solve('20 5 /'))
# print(solve('10 4 - 3 *'))
# print(solve('2 3 4 * +'))
# print(solve('2 3 + 4 *'))
# print(solve('20 5 - 3 -'))
# print(solve('100 20 5 / /'))

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if self.is_empty():
            return -1
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return -1
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0

# qu = Queue()
# print(qu.dequeue())
# qu.enqueue(1)
# qu.enqueue(2)
# qu.enqueue(3)
# print(qu.queue)
# qu.dequeue()
# print(qu.queue)
# print("-"*10)
# print(qu.is_empty())
# print(qu.front())
# print(qu.queue)
# print(qu.dequeue())
# print(qu.queue)

# class Bank:
#     def __init__(self):
#         self.waits = Queue()
#     def enqueue(self, newone):
#         self.waits.enqueue(newone)
#         print(f"현재 대기열: {self.waits.queue}")
#     def dequeue(self):
#         print(f"업무 처리 중인 고객: {self.waits.dequeue()}")
#         self.get_status()
#         return
#     def get_status(self):
#         print(f"남은 대기 고객: {self.waits.queue}")

# bank = Bank()
# bank.enqueue("김철수")
# bank.enqueue("이영희")
# bank.enqueue("박민수")
# bank.dequeue()

# class Deque():
#     def __init__(self):
#         self.deque = []

#     def push_front(self, x):
#         self.deque = [x] + self.deque

#     def push_back(self, x):
#         self.deque.append(x)

#     def pop_front(self):
#         if self.is_empty():
#             return -1
#         return self.deque.pop(0)
    
#     def pop_back(self):
#         if self.is_empty():
#             return -1
#         return self.deque.pop()

#     def is_empty(self):
#         return len(self.deque) == 0

# dq = Deque()
# print(dq.is_empty())
# print(dq.pop_back())
# print(dq.pop_front())
# dq.push_front(1)
# dq.push_back(2)
# dq.push_front(3)
# dq.push_back(4)
# dq.push_front(5)
# print(dq.deque)
# dq.pop_back()
# print(dq.deque)
# dq.pop_back()
# print(dq.deque)
# dq.pop_front()
# print(dq.deque)

# print("-"*10)
# print(dq.is_empty())