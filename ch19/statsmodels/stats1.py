# stats1.py
import statsmodels.api as sm

data = sm.datasets.get_rdataset("mtcars").data
# print(data)
# print(type(data))

# # 가설 : 자동차의 힘(마력)이 좋으면 연비가 낮을 것이다.
# X = data['hp']    # 독립변수
# y = data['mpg']   # 종속변수

# # 상수항 추가
# X = sm.add_constant(X)
# # print(X)

# # 모델 생성 및 학습
# # obj = sm.OLS()
# # model = obj.fit()
# model = sm.OLS(y, X).fit()

# print(model.summary())

# 가설 : 자동차의 힘(마력)이 좋으면 연비가 낮을 것이다.
# 가설 : 자동차의 무게가 가벼우면 연비가 좋을 것이다.
X = data[['hp', "wt"]]    # 독립변수
y = data['mpg']   # 종속변수

# 상수항 추가
X = sm.add_constant(X)
# print(X)

# 모델 생성 및 학습
# obj = sm.OLS()
# model = obj.fit()
model = sm.OLS(y, X).fit()

print(model.summary())
print(model.params)
print(model.params["const"])
print(model.params["hp"])
print(model.params["wt"])