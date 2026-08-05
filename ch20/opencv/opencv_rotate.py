# opnecv_rotate.py

import cv2

image = cv2.imread(r"ch20\sample.jpg")

print(image.shape)
(h, w) = image.shape[0 : 2] # 가로, 세로, 채녈
center = (w/2, h/2)
# 1. 회전 행렬 생성
# cv2.getRotationMatrix2D(center, angle, scale)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()