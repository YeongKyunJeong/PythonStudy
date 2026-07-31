# pd_data.py

import pandas as pd

## 데이터 탐색 / 분석
# CSV 파일 데이터 읽기
df_csv = pd.read_csv(r"C:\ROKEY\py_work\ch18\data.csv")
# print(type(df_csv))
# print(df_csv)

# df_csv = pd.read_csv(r"C:\ROKEY\py_work\ch18\data.csv", header = None)
# print(type(df_csv))
# print(df_csv)

# print("-"*20)

# path = r"ch18\data.xlsx"
# df_xl = pd.read_excel(path)
# print(type(df_xl))
# print(df_xl)

# print("-"*20)

# print(df_csv.head())
# print(df_csv.head(3))
# print(df_csv.head(None))
# print(df_csv.tail())
# print(df_csv.tail(3))

# print("-"*20)

# df_csv.info()

# 기술 통계량 정보
# print(df_csv.describe())

# 랜덤 샘플링
# print(df_csv.sample(2))           # 개수로 샘플링
# print(df_csv.sample(frac = 0.5))  # 비율로 샘플링

