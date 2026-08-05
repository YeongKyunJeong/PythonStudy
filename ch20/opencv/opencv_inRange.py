# opnecv_inRange.py

import cv2
import numpy as np

# 이미지 로드
image = cv2.imread(r"ch20\candy.jpg")

# HSV로 변환 -> 색상을 한 채녈(Hue)로 처리
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

green_lower = np.array([35, 100, 100])
green_upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, green_lower, green_upper)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Green Color Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 초록색의 HSV 색상 범위 설정 (초록색의 상한값과 하한값 지정)
# Hue : 색을 0~179까지 범위의 값으로 표현
# OpneCV에서는 0 ~ 360도를 8비트(0 ~ 255)로 표현하지 않고 **0 ~ 179** 범위로 표현
# 0 -> 빨강
# 30 -> 주황
# 60 -> 노랑
# 120 -> 초록
# 180 -> 청록 (Cyan)
# 240 -> 파랑
# 300 -> 자홍 (Magenta)

# Hue 범위 기준표
# 색상          H 범위 (대략적)     설명
# 빨강          0~10, 170~180       
# 주황          10~25
# 노랑          25~35
# 