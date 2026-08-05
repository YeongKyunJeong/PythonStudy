# violin_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터셋 로드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
# sns.set_theme(style = "whitegrid")  # 기본 테마 설정

# 3. 그래프 표시
sns.violinplot(data = iris,
                x = "species",
                y = "sepal_length",
                inner = "quart" # 사분위값 표시, 기본 : 박스 표시
                )
# plt.boxplot(data)
plt.title("Violing Plot Example")
plt.show()