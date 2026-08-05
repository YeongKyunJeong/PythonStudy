# iris.py
from sklearn.datasets import load_iris
import pandas as pd
from sklearn import svm
from sklearn import metrics

# ### 데이터 수집 및 전처리
# # 1-1. iris 데이터셋 로드
# iris = load_iris()
# # print(iris)

# df = pd.DataFrame(data = iris.data,
#              columns = iris.feature_names)
# df['target'] = iris.target
# # print(df.head())

# target_names = {
#     0:iris.target_names[0],  # setosa
#     1:iris.target_names[1],  # versicolor
#     2:iris.target_names[2],  # virginica
#     }
# # Dictionary에서 해당하는 키를 찾아 값으로 바꿔주는 메서드
# df['target'] = df['target'].map(target_names)
# # print(df.head())

# # 1-2. 필요한 열 추출하기
# iris_data = df[[
#     "sepal length (cm)",
#     "sepal width (cm)",
#     "petal length (cm)",
#     "petal width (cm)"]]
# iris_label = df["target"]
# # print(iris_data)
# # print(iris_label)

# from sklearn.model_selection import train_test_split
# # 1-3. 학습 전용 데이터와 테스트 전용 데이터 분리
# # 기본 분할 비율 : 75% : 25%
# train_data, test_data, train_label, test_label = \
#     train_test_split(iris_data, iris_label)
#     # option에 test_size = 0.3 => 테스트 사이즈 30%로 가능
# # print(train_data)

# # 2. 알고리즘 선택
# clf = svm.SVC()

# # 3. 학습/훈련 => 모델 생성
# clf.fit(train_data, train_label)

# # 4. 예측
# pre = clf.predict(test_data)

# # 5. 정확도 평가
# ac_score = metrics.accuracy_score(test_label, pre)
# # print(f"정답률 : {ac_score}")

from sklearn.datasets import load_iris
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd

data_iris = load_iris()
# print(data_iris.keys())
# print(data_iris.target)
# print(data_iris.target_names)
df_iris = pd.DataFrame(data_iris.data,
                        columns = data_iris.feature_names)
df_iris['target'] = data_iris.target
target_to_name = {0: data_iris.target_names[0],
                  1: data_iris.target_names[1],
                  2: data_iris.target_names[2]}
df_iris['target'] = df_iris['target'].map(target_to_name)
# print(df_iris.sample(10))

# print(df_iris.columns[:4])
iris_data = df_iris[df_iris.columns[:4]]
# print(iris_data)
iris_label = df_iris[df_iris.columns[-1]]
# print(iris_label)

data_train, data_test, label_train, label_test = \
    train_test_split(iris_data, iris_label)

clf = svm.SVC()
clf.fit(data_train, label_train)

pre = clf.predict(data_test)

accuracy = metrics.accuracy_score(label_test, pre)
print(f"정확도 : {accuracy}")