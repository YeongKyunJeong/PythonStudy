# practice.py

class Deque:
    def __init__(self):
        self.deque = []

    def append_left(self, x):
        self.deque = [x] + self.deque
        
    def append(self, x):
        self.deque.append(x)

    def pop(self):
        if self.is_empty():
            return -1
        return self.pop()
    
    def pop_left(self):
        if self.is_empty():
            return -1
        return self.pop(0)

    def is_empty(self):
        return len(self.deque) == 0

    def rotate(self, i):
        if self.is_empty():
            return -1
        i %= len(self.deque)
        self.deque = self.deque[i:] + self.deque[:i]
        print(self.deque)
        return

dq = Deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)
dq.append(6)
dq.append(7)
dq.append(8)
dq.rotate(1)
dq.rotate(-1)
dq.rotate(2)
dq.rotate(-2)
dq.rotate(-3)
dq.rotate(3)