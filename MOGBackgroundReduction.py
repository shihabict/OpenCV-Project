import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
print(fgbg)

while True:
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('Orginal',frame)
    cv2.imshow('Orginal', fgmask)




    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()