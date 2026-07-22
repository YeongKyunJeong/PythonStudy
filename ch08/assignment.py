# assignment.py

# a = [1, 2, 3, 4]
# a[0], a[3] = a[3], a[0]
# print(a)

# lst = [40, 20, 30, 10]

# lst[0], lst[3] = lst[3], lst[0]
# print(lst)

# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]

# print(arr)

# a = [1, 2, 3]
# b = a
# print(id(a) == id(b))

# x = 42
# y = 42
# print(id(x) == id(y))

# def funca():
#     print("funca")
#     return False

# def funcb():
#     print("funcb")
#     return True

# if funca() and funcb():
#     print("Done")

# if funcb() or funca():
#     print("Done")

a = [3, 6, 7, 4, 9, 10, 13]
# idx_first_even = -1
# idx_last_odd = -1
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         if idx_first_even < 0 :
#             idx_first_even = i
#     else:
#         idx_last_odd = i
# a[idx_first_even], a[idx_last_odd] = a[idx_last_odd] ,a[idx_first_even]
# print(a)

# def fmax(lst):
#     max_val = lst[0]
#     for num in lst:
#         if max_val < num:
#             max_val = num
#     return max_val
# print(fmax(a))

# data = [29, 10, 14, 37, 13]

# for i in range(1):
#     idx = i
#     for j in range(len(data)):
#         if data[idx] > data[j]:
#             idx = j

#     data[idx], data[i] = data[i], data[idx]

# print(data)

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # 빈칸에 들어갈 코드
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# data = [64, 25, 12, 22, 11]
# print(selection_sort(data))

dict1 = { 'a': 10, 'b': 20, 'c': 30 }

def sumdict(dict1):
    sum = 0
    for val in dict1.values():
        sum += val
    return sum

print(sumdict(dict1))