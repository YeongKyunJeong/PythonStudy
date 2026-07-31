# assignment.py

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.xlabel('X-axis')
# plt.xlabel('Y-axis')
# plt.show()

# import pandas as pd
# df = pd.read_csv(r"ch18\data.csv", sep= " ")
# columns = df.columns
# # print(f"{columns[1]} 평균: {df[columns[1]].mean()}, 최댓값: {df[columns[1]].max()} 최솟값: {df[columns[1]].min()}")
# # print(f"{columns[2]} 평균: {df[columns[2]].mean()}, 최댓값: {df[columns[2]].max()} 최솟값: {df[columns[2]].min()}")


# print(df[(df["Age"] >= 30) & (df["Salary"] >= 60000) ])

# import numpy as np
# arr = np.array([n for n in range(1, 11)])
# arrsqr = arr*arr
# print(f"원본 배열: {arr}")
# print(f"제곱 배열: {arrsqr}")
# print(f"평균: {arrsqr.mean()}, 최댓값: {arrsqr.max()}, 최솟값: {arrsqr.min()}")

# import numpy as np
# arr = np.random.randint(1, 13, (3, 4))
# print(arr.max(axis = 1))

from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8 ,10]
plt.plot(x, y)
plt.title("Title")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.grid()
plt.show()