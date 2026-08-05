# assignment.py

# import statsmodels.api as sm
# import pandas as pd

# x = pd.DataFrame([1, 2, 3, 4, 5], columns = ["x"])
# y = pd.DataFrame([2, 4, 6, 8, 10], columns = ["y"])

# x = sm.add_constant(x)

# model = sm.OLS(y, x).fit()

# print(model.summary())


# import statsmodels.api as sm
# import pandas as pd

# x = pd.DataFrame([1, 2, 3, 4, 5], columns = ["x"])
# y = pd.DataFrame([2, 4, 6 ,8 ,10], columns = ["y"])

# x = sm.add_constant(x)
# model = sm.OLS(y, x).fit()
# # print(model.params)
# # print(model.params['x'])
# # print(model.params['const'])

# # print(x['x'][0])
# # print(len(x['x'])-1)
# # print(x['x'][len(x['x'])-1])

# import matplotlib.pyplot as plt
# import numpy as np

# xs = np.linspace(x['x'][0], x['x'][len(x)-1], 100)
# ys = model.params['x']*xs + model.params['const']

# plt.scatter(x['x'], y['y'])
# plt.plot(xs, ys, color = "red")
# plt.title("Linear Regression")
# plt.savefig('ch19/ols.png')
# plt.show()

# from sklearn import svm
# import pandas as pd
# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# clf = svm.SVC()
# clf.fit(X, y)

# print(clf.predict([[4.5], [6.5]]))

# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# from sklearn import svm
# clf = svm.SVC()
# clf.fit(X, y)
# print(clf.predict([[4.5], [6.5]]))

# import scipy.optimize as sp
# def equation(x):
#     return (x-3)**2
# print(sp.root(equation, 1).x)

# import scipy.stats as spst
# groupA = [80, 85, 90, 75, 95]
# print(spst.describe(groupA))

# class ListIterator:
#     def __init__(self, data):
#         if not isinstance(data, list):
#             raise TypeError("리스트를 입력해야 합니다.")
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.data):
#             value = self.data[self.index]
#             self.index += 1
#             return value
#         else:
#             raise StopIteration()

# mylist = [1, 2, 3, 4, 5]
# iterator = ListIterator(mylist)

# for item in iterator:
#     print(item)

# def from1ton(n):
#     for num in range(1, n+1):
#         yield num*num

# gen = from1ton(10)
# for sqr in gen:
#     print(sqr)

# class Stack:
#     def __init__(self):
#         self.stack = ["두산", "로키", "부트"]

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return

#     def peak(self):
#         if not self.is_empty():
#             return self.stack[-1]

#     def is_empty(self):
#         return len(self.stack) == 0

#     def status_stack(self):
#         return self.stack

# stack = Stack()
# stack.push("캠프")
# print(stack.status_stack())

# stack.pop()
# print(stack.status_stack())

# graph = {"두" : ["산", "로", "키"],
#          "산" : ["두", "부"],
#          "로" : ["두"],
#          "키" : ["두", "트"],
#          "부" : ["산"],
#          "트" : ["키", "캠", "프"],
#          "캠" : ["트"],
#          "프" : ["트"]}

# def graphdfs(graph, start):
#     stack = [start]
#     visited = {start}
#     order = []

#     while stack:
#         cur = stack.pop()
#         order.append(cur)

#         for nxt in reversed(graph[cur]):
#             if nxt in visited:
#                 continue
#             stack.append(nxt)
#             visited.add(nxt)

#     return order

# print(graphdfs(graph, "두"))

# from collections import deque
# def graphbfs(graph, start):
#     queue = deque()
#     queue.append(start)
#     visited = {start}
#     order = []

#     while queue:
#         cur = queue.popleft()
#         order.append(cur)

#         for nxt in graph[cur]:
#             if nxt in visited:
#                 continue
#             queue.append(nxt)
#             visited.add(nxt)

#     return order

# print(graphbfs(graph, "두"))

# import pandas as pd
# path = r"대구광역시 동구_연도별 체납차량 번호판 영치실적_20251031.csv"
# df = pd.read_csv(path, encoding = "cp949")
# # print(df)

# # with open(path, "r") as f:
# #     data = f.readlines()
# #     columns = data[0].strip().split(",")
# #     for i in range(1, len(data)):
# #         data[i] = data[i].strip().split(",")
# #     df = pd.DataFrame(data[1:], columns = columns)
# # print(df)

# import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = "Malgun Gothic"

# plt.plot(df["년도"], df["영치대수"])
# plt.xlabel("년도")
# plt.ylabel("영치대수")
# plt.title("연도별 영치대수")
# plt.savefig("연도별 영치대수.png")
# plt.show()

# import numpy as np
# import statsmodels.api as sm

# X = np.array([1, 2, 3, 4, 5])
# y = np.array([1, 2, 3, 4, 5])

# X = sm.add_constant(X)

# model = sm.OLS(y, X).fit()

# W = model.params[1]
# print("기울기 (coef):", W)
# # print(model.summary())

# import scipy.optimize as spop
# def equation(x):
#     return x**2 + 6*x + 9
# print(spop.root(equation, 0).x)

# lst = ["1", "2", "3", "4", "5", "6"]
# del lst[3]
# print(lst)
# del lst[3]
# print(lst)
# lst.remove("2")
# print(lst)

a = [3, 6, 7, 4, 9, 10, 13]

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         evenindex = i
#         break

# for j in range(len(a)-1, -1, -1):
#     if a[j] % 2 == 1:
#         oddindex = j
#         break

# a[evenindex], a[oddindex] = a[oddindex], a[evenindex]
# import random
# print(random.choice(a))
# print(random.sample(a, 4))

