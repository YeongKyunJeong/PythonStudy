# opencv_blur.py

import cv2
image = cv2.imread(r"ch20\sample.jpg")

# blurred = cv2.GaussianBlur(image, (5, 5), 0)
blurred = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("GaussianBlur", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 블러 함수에서 커널 크기는 홀수
# 홀수 크기 커널이어야 중앙 픽셀이 존재하여 대칭적 처리 가능
# 픽셀 주변 값 평균/가중평균 등으로 처리

# sigma란?
# GaussianBlur() 함수에서의 sigma는 가우시안 커널의 표준편차를 의미
# 얼마나 흐릿하게 블러를 줄 것인지에 영향을 줌
# sigmaX가 크면 더 넓게 퍼짐 => 더 강한 Blur
# sigmaX를 정하는 절대 공식은 없고,
# 보통 커널 크기에 따라 경험식 또는 실험식으로 결정