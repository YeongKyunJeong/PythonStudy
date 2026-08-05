# xor2.py

from sklearn import svm
from sklearn import metrics
import pandas as pd

# 1. 데이터 수집 및 전처리
#            P  Q result
xor_data = [[0, 0, 0],
            [0, 1, 1], 
            [1, 0, 1],
            [1, 1, 0]]

# 데이터 가공 - 학습을 위해 데이터와 레이블 분리하기
xor_df = pd.DataFrame(xor_data)

# 학습 데이터 (독립 변수)
data = xor_df.loc[:, 0:1]

# 학습 레이블 (종속 변수)
label = xor_df.loc[:, 2]

# 2. 알고리즘 선택
clf = svm.SVC()

# 3. 학습/훈련 => 모델 생성
clf.fit(data, label)

pre = clf.predict(data)
print(pre)
print(type(pre))

ac_score = metrics.accuracy_score(label, pre)
print(f"정답률 : {ac_score}")