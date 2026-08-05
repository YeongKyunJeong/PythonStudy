# linear_regression.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터셋 로드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
# sns.set_theme(style = "whitegrid")  # 기본 테마 설정

# 3. 그래프 표시
sns.lmplot(data = iris,
                x = "sepal_length",
                y = "sepal_width",
                hue="species",
                height = 3) # height : 그래프를 그리는 영역의 자체 높이(인치)
                            #       -> 그래프가 표시되는 크기
                            # 선 옆 반투명 음영 : 회귀선의 신뢰구간 (Confidence Interval)
# plt.plot(x, y)
plt.title("Linear Regression Plot")
plt.show()