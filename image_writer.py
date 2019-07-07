import cv2
#starting camera
cap=cv2.VideoCapture(0)
#adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# saving video                                width,height
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))
'''
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    output.write(frame)   #sending data to video write
    if cv2.waitKey(10)  & 0xff == ord('q') :
        break
cv2.destroyAllWindows() # this will destroy all windows
cap.release()
'''
while cap.isOpened():
    status,frame=cap.read()
     #converting image into a grey scale
    graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
     # line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
     #rectangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),2)
     # circle
    cv2.circle(frame,(200,300),100,(13,14,123),2)
     # text writing
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'OpenCV',(10,500),font,2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame)
    cv2.imshow('livegray',graying)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

