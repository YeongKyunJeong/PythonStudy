# opencv_resize.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"ch20\sample.jpg")

resized = cv2.resize(image, (300, 300))
# 이미지 창에 표시
cv2.imshow("Resized Image", resized)
cv2.waitKey(0) # 키 입력을 기다림, 키가 입력되면 창 닫기
cv2.destroyAllWindows() # 프로그램이 끝날 때 OpneCV로 연 창을 모두 닫기