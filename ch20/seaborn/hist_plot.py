# hist_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# # 1. 샘플 데이터셋 로드
# iris = sns.load_dataset("iris")

# # 2. 기본 스타일 설정
# # sns.set_theme(style = "whitegrid")  # 기본 테마 설정

# # 3. 그래프 표시
# sns.histplot(data = iris,
#                 x = "sepal_length",
#                 hue="species",
#                 kde = True) # 커널 밀도 추정 : 분포 곡선 추정
# # plt.hist(data, bins = 4, color = "skyblue", edgecolor = "black")
# plt.title("Histogram Example")
# plt.show()

# 1. 샘플 데이터셋 로드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
# sns.set_theme(style = "whitegrid")  # 기본 테마 설정

# 3. 그래프 표시
sns.histplot(data = iris,
                x = "sepal_length",
                y = "petal_length", # 2차원에 대한 분포
                hue="species",
                kde = True) # 커널 밀도 추정 : 분포 곡선 추정
# plt.hist(data, bins = 4, color = "skyblue", edgecolor = "black")
plt.title("Histogram Example")
plt.show()