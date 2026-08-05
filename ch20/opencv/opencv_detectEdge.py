# opencv_detectEdge.py

import cv2

image = cv2.imread(r"ch20\sample.jpg")

edges = cv2.Canny(image, 100, 200)

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Canny 알고리즘
# cv2.Canny() 같은 엣지 검출 함수에서 사용하는 threshold 수치들은
# 색상 코드가 아니라 "픽셀 강도(intensity)" 값을 의미
# 픽셀 강도(intensity) : 픽셀 하나가 얼마나 밝거나 어두운지 나타내는 값

# 예)
# 200 이상 -> 강한 엣지로 인식
# 100 ~ 200 사이 -> 주변에 강한 엣지가 있으면 유지
# 100 미만 -> 무시함