# scatter_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터셋 로드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
sns.set_theme(style = "whitegrid", palette = "pastel")

# 3. 그래프 표시
sns.scatterplot(data = iris,
                x = "petal_length",
                y = "petal_width",
                hue="species",
                style = "species") # style : 점 모양
# plt.scatter(x, y, color = "#45EB45", edgecolors =  "#125A12")
plt.title("Scatter Plot Example")
plt.show()

