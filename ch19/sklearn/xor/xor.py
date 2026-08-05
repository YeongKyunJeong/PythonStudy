# xor.py

# import sklearn as sk
from sklearn import svm
from sklearn import metrics

# 1. 데이터 수집 및 전처리 -> XOR은 데이터가 적어서 필요 없음

# 2. 알고리즘 선택
clf = svm.SVC()

# 3. 학습/훈련 => 모델 생성
clf.fit([[0, 0],
         [0, 1],
         [1, 0],
         [1, 1]],
         [0, 1, 1, 0])

pre = clf.predict(
    [[0, 1], [1, 1]]
)
print(pre)
print(type(pre))

ac_score = metrics.accuracy_score([1, 0], pre)
print(f"정답률 : {ac_score}")