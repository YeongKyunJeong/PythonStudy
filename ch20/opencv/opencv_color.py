# opencv_color.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"ch20\sample.jpg")

# OpenCV의 기본 채녈 설정 : BGR
# 이미지 연산의 양을 줄여서 속도를 높임
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# H(Hue, 색조), S(Saturation, 채도), V(Value, 명도)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 이미지 창에 표시
# cv2.imshow("Grayscale Image", gray)
# cv2.imshow("RGB Image", rgb)
cv2.imshow("HSV Image", hsv)
cv2.waitKey(0) # 키 입력을 기다림, 키가 입력되면 창 닫기
cv2.destroyAllWindows() # 프로그램이 끝날 때 OpneCV로 연 창을 모두 닫기
