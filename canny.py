import cv2
import numpy as np
path="C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 104828.png"
img=cv2.imread(path)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
imgcanny=cv2.Canny(imgblur,100,200)
cv2.imshow("ori",img)
cv2.imshow("canny",imgcanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
