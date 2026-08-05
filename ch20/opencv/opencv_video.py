# opencv_video.py
# 실시간 영상 처리

import cv2
import time

cap = cv2.VideoCapture(r"ch20\turtle.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # cv2.imshow("Video", frame)
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("Edge Detection", edges)
    if cv2.waitKey(2) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()