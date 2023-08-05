from cvzone.HandTrackingModule import HandDetector
import cv2

model = HandDetector()

cap=cv2.VideoCapture()
status,photo=cap.read()
cv2.waitKey()
cv2.destroyAllWindows()
