import numpy as  np
import cv2
img = cv2.imread('dog.jpeg',1)
print(img)
print(img.shape)
cv2.imshow('dog',img)
cv2.imshow('dog1',img-50)
cv2.imshow('dog2',img[0:200,0:600]+100)
cv2.imshow('dog3',img/2)
cv2.waitKey(0)
cv2.destroyAllWindows()
