# pd_data1.py

import pandas as pd
data = {
    'ID' : [1, 2, 3],
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [30, 35, 25]
}
df = pd.DataFrame(data)
# print (df)

# # 데이터 필터링
# print(df["Name"])              # 열 선택
# print(df["Age"])               # 열 선택

# print("-"*20)

# 데이터 필터링
# filterd = df[ df["Age"] > 27]    # [] 안에 조건 추가 -> Boolean Series 생성
# print(filterd["Age"])            # 행 필터링
# filterd = df.loc[ df["Age"] > 27, ['Name', 'Age']] # loc 이용, 행과 열 동시 필터링 
# print(filterd)

# print("-"*20)
# 데이터 정렬
# sorted_df = df.sort_values(by = 'Age')                     # 오름차순
# sorted_df = df.sort_values(by = ['Age', 'ID'], ascending = False)  # 내림차순
# print(sorted_df)

df['Salary'] = [5000, 6000, 7000]
# df['Salary'] = [5000, 6000,]
# print(df)
df.loc[3] = [4, 'David', 40, 8000]
# df.loc[6] = [4, 'David', 40, 343]
# print(df)

df = df.drop(1)
# print(df)

# print("-"*20)
data2 = {
    'ID' : [5, 6],
    'Name' : ['Eve', 'Frank'],
    'Age' : [28, 33]
}

# 데이터 행 병합
df2 = pd.DataFrame(data2)
# print(df2)
concated = pd.concat([df, df2])
# print(concated)
# concated = concated.reset_index()
# print(concated)
# 데이터 인덱스 재정렬
concated = concated.reset_index(drop = True)
# print(concated)
concated2 = pd.concat([df, df2], ignore_index = True)
# print(concated2)

# print("-"*20)
# 데이터 열 병합
# 병합시 기준 필요
data3 = {
    "ID" : [1, 2, 3, 4, 5, 6],
    'Department' : ["HR",
                    "Engineering",
                    "Sales",
                    "R&D",
                    "Finance",
                    "Sales"]
}
df3 = pd.DataFrame(data3)
# print(df3)
merged = pd.merge(concated, df3)
# print(merged)

# print("-"*20)
# 데이터 처리
# 결측치 찾기
print(merged.isnull())
print(merged.isnull().sum())

# 결측치 채우기
meanval = merged['Salary'].mean()
merged['Salary'] = merged['Salary'].fillna(meanval)
print(merged)

# print("-"*20)
# print(merged['Salaty'].count())
# print(merged['Salaty'].std())
# print(merged['Salaty'].min())
# print(merged['Salaty'].max())
# print(merged['Salaty'].quantile(0.25))
# print(merged['Salaty'].quantile(0.5))
# print(merged['Salaty'].quantile(0.75))

# print("-"*20)
# 중복 데이터 처리
data1 = {
    'ID' : [1, 3],
    'Name' : ["Alice", "Charlie"],
    'Age' : [30, 25],
    'Salary' : [5000, 7000],
    'Department' : ["HR", "Sales"]
}
df1 = pd.DataFrame(data1)
df1 = pd.concat([merged, df1])
print(df1.duplicated())
print(df1)

# df1_1 = df1.drop_duplicates()
# print(df1_1)
# df1_1 = df1_1.drop(0)
# print(df1_1)
# # df1_1 = df1_1.drop(0) # KeyError 발생
# # print(df1_1)

# df1_2 = df1.drop(0)
# print(df1_2)