# Sorting.py

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        minidx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(selection_sort([5, 3, 1, 4, 2])) # [1, 2, 3, 4, 5]
print(bubble_sort([5, 3, 1, 4, 2])) # [1, 2, 3, 4, 5]
print(insertion_sort([5, 3, 1, 4, 2])) # [1, 2, 3, 4, 5]

print("-"*10)
# Python 리스트 정렬 함수
# Sorted(리스트, key = 정렬_함수) : 오름차순 기본
numbers = [5, 3, 1, 4, 2]
print(sorted(numbers, key = lambda x: x))

# 리스트.sort(key = 정렬_함수) : 오름차순 기본
numbers.sort(key = lambda x: x)
print(numbers)

# 내림차순 정렬
print(sorted(numbers, key = lambda x: -x))
numbers.sort(key = lambda x : -x)
print(numbers)

print(sorted(numbers, key = lambda x: x, reverse = True))
numbers.sort(reverse = True)
print(numbers)