# matplotlib_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정 : 해당 설정을 해야 한글이 정상 출력됨
plt.rcParams["font.family"] = "Malgun Gothic"

# # 간단한 선 그래프
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y)
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# # Bar Chart
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.title("Bar Chart")
# plt.show()

# # Histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4]
# plt.hist(data, bins = 4, color = "skyblue", edgecolor = "black")
# plt.title("Histogram")
# plt.show()

# # Scatter Plot
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
# plt.scatter(x, y, color = "#45EB45", edgecolors =  "#125A12")
# plt.title("Scatter Plot")
# plt.show()

# # Pie Chart
# size = [15, 30, 45, 10]
# labels = ["Group A", "Group B", "Group C", "Group D"]
# plt.pie(size, labels = labels, autopct = "%1.1f%%", startangle = 90)
# plt.title("Pie Chart")
# plt.show()

# # Box Plot
# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# print("-"*20)
# 그래프 커스터마이징
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y, color = "red", linestyle = "--", marker = "o")
# plt.plot(x, y, "ro--")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y, "k^:")
# plt.xlim(0, 5)
# plt.ylim(0, 40)
# plt.xticks(range(1, 5))
# plt.yticks(range(0, 41, 10))
# plt.show()

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# x1 = [1, 2, 3, 4]
# y1 = [3, 5, 9, 7]
# plt.plot(x, y, label = "Data 1")
# plt.plot(x1, y1, label = "Data 2")
# plt.legend(loc = "upper left")
# plt.savefig(r"Python_Basic\ch18\matplotlib\my_plot.png")
# plt.show()

print("-"*20)
# Subplot 활용1
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4]

# fig : 전체 그래프 창
# axs : 각 subplot(그래프 영역)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
fig.suptitle("전체 그래프 제목")
plt.tight_layout
plt.show()