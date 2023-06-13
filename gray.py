import cv2
import numpy as np
path="C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 104828.png"
img=cv2.imread(path)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("ori",img)
cv2.imshow("gray",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()
