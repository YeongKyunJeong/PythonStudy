# facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

# 복합 그래프 작성

# 1. 샘플 데이터셋 로드
tips = sns.load_dataset("tips")
# print(tips.head(30))

# 2. 기본 스타일 설정
sns.set_theme(style = "dark", palette = "pastel")

# 3. 복합 그래프 설정
g = sns.FacetGrid(tips, col = "time", row = "sex",
                  height = 3.5, aspect = 0.95)

# 4. 그래프 표시
# g.map_dataframe(sns.scatterplot, 
#                 x = "total_bill",
#                 y = "tip"
# )

g.map_dataframe(sns.histplot, 
                x = "total_bill")

g.set_titles(row_template = "sex : {row_name}", col_template = "{col_name}")

plt.tight_layout()
plt.show()
