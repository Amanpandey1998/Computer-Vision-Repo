import cv2
# starting camera
cap=cv2.VideoCapture(0)
if cap.isOpened():
	print("camera is ready to take pictures")
else:
	print("check your web cam drivers")
status,frame=cap.read()
cv2.imshow('live',frame)
cv2.waitKey(0)
cv2.destroyWindow('live')
# to close camera
cap.release()
