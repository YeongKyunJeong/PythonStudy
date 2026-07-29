# queue_list.py

# 빈 큐 구현
queue = []

# enqueue
queue = []
queue.append(1)
print(f"queue : {queue}")
queue.append(2)
print(f"queue : {queue}")
queue.append(3)
print(f"queue : {queue}")
queue.append(4)
print(f"queue : {queue}")

# dequeue
queue.pop(0)
print(f"queue : {queue}")
queue.pop(0)
print(f"queue : {queue}")
queue.pop(0)
print(f"queue : {queue}")
if queue == []:
    print("is empty")
else:
    queue.pop(0)
    print(f"queue : {queue}")
if queue == []:
    print("is empty")
else:
    queue.pop(0)
    print(f"queue : {queue}")