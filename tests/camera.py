import cv2,time


video = cv2.VideoCapture(0)

ret,frame = video.read()
img_name="test.png"
cv2.imwrite(img_name,frame)

video.release()
