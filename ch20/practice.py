# practice.py

# from sklearn import svm
# from sklearn import metrics

# clf = svm.SVC()
# clf.fit([[0, 0],
#          [0, 1],
#          [1, 0],
#          [1, 1]],
#         [0, 1, 1, 0])
# pre = clf.predict([[1, 0]])
# acc = metrics.accuracy_score([1], pre)
# print(acc)

# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# import pandas as pd
# iris = load_iris()
# df = pd.DataFrame(data = iris.data, columns = iris.feature_names)
# print(df.head())

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.random.normal(loc = 50, scale = 10, size = 1000)
# sns.histplot(data, bins = 30, kde = True)
# plt.title("Normal Distribution")
# plt.show()