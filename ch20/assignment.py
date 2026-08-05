# assignment.py

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = np.random.normal(loc = 50, scale = 10, size = 1000)
# sns.histplot(data, kde = True)
# plt.title("Normal Distribution")
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset('tips')
# sns.boxplot(tips, x = "day", y = "total_bill")
# plt.title("tips Box Plot")
# plt.show()

# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# cv2.imshow("cv2 Image Loading",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray scale", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 엣지 검사
# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edge = cv2.Canny(gray, 100, 200)
# cv2.imshow("edge", edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 가우시안 블러
# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# blurred = cv2.GaussianBlur(image, 
#                            (15, 15),
#                              0)
# cv2.imshow("Gaussian Blur", blurred)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 리사이즈
# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# resized = cv2.resize(image, (200, 100))
# cv2.imshow("resizes", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 회전
# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# h, w = image.shape[:2]
# M = cv2.getRotationMatrix2D((w/2, h/2), 45, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("rotated", rotated)
# cv2.waitKey()
# cv2.destroyAllWindows()

# import cv2
# image = cv2.imread(r"Python_Basic\ch20\sample.jpg")
# h, w = image.shape[:2]
# M = cv2.getRotationMatrix2D((w/2, h/2), 60, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# image = cv2.imread(r"Python_Basic\ch20\peaple.jpg")

# face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# face_cascade = cv2.CascadeClassifier(face_path)

# faces = face_cascade.detectMultiScale(image = image,
#                                       scaleFactor = 1.1,
#                                       minNeighbors = 5,
#                                       minSize = (300, 300),
#                                       maxSize = (1000, 1000)
# )
# for x, y, w, h in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (200, 0, 0), 2)

# cv2.imshow("face detection", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.set_theme(style = "whitegrid", palette = "bright")

# sns.lmplot(data = iris, x= "sepal_length", y = "sepal_width",
#            hue = "species",)

sns.pairplot(data = iris, hue = 'species')

# g = sns.FacetGrid(data = iris, col = "species")
# g.map_dataframe(sns.histplot, x = "sepal_length", kde = True)
# # g.map_dataframe(sns.scatterplot, x = "sepal_length", y = "sepal_width")
# g.set_titles(col_template = "species : {col_name}")
plt.show()