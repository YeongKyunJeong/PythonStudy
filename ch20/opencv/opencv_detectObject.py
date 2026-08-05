# opencv_detectObject.py

import cv2
import matplotlib.pyplot as plt

# 이미지 파일 읽기
image = cv2.imread(r"ch20\peaple.jpg")

face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_path)

# 이미지를 그레이 스케일로 변환 -> 더 빠르게 처리
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출 수행
# scaleFactor : 이미지 크기를 줄여가면서 검출(1.1배씩 감소 = 10%)
# 사람마다 얼굴 크기가 다르므로 이미지를 축소하면서 얼굴을 탐색
# minNeighbot : 객체로 인지되기 위한 최소 중복 검출 수
# 보통 4 ~ 6 정도가 안정적
# minSize : 최소 객체 크기 (선택 사항) => 이보다 작은 객체는 얼굴로 간주하지 않음
# maxSize : 최대 객체 크기 (선택 사항)
faces = face_cascade.detectMultiScale(gray,
                              scaleFactor = 1.1,
                              minNeighbors = 5,
                              minSize = (200, 200))
print(faces) # [x, y, w, h]

# 검출된 객체에 사각형 표시
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (200, 0, 0), 2)

# # 이미지 창에 표시
cv2.imshow("Face Detection", image)
cv2.waitKey(0) # 키 입력을 기다림, 키가 입력되면 창 닫기
cv2.destroyAllWindows() # 프로그램이 끝날 때 OpneCV로 연 창을 모두 닫기

# import cv2

# image = cv2.imread(r"ch20\peaple.jpg")

# face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# face_cascade = cv2.CascadeClassifier(face_path)

# faces = face_cascade.detectMultiScale(gray,
#                                       scaleFactor = 1.1,
#                                       minNeighbors = 5,
#                                       minSize = (200, 200))
# for x, y, w, h in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 200), 2)

# cv2.imshow(" ",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
