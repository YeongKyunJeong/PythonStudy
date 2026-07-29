# queue_class.py
# 큐 구현 : 클래스 활용

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def status_queue(self):
        return self.queue


if __name__ == "__main__":
    q1 = Queue()
    print(q1.dequeue())
    q1.enqueue(1)
    q1.enqueue(2)
    q1.dequeue()
    print(q1.status_queue())
    q1.enqueue(3)
    q1.enqueue(4)
    print(q1.status_queue())


class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if self.is_empty():
            return
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def queue_status(self):
        return self.queue