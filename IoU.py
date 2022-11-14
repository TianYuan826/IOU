# 

import cv2
import numpy as np

# define 

def CountIOU(RecA, RecB):
    x0 = max(RecA[0], RecB[0])
    y0 = max(RecA[1], RecB[1])
    x1 = min(RecA[2], RecB[2])
    y1 = min(RecA[3], RecB[3])
    
    # caculate the area of the intersection
    Area_Inter = max(0, x1 - x0) * max(0, y1 - y0)

    # caculate the area of the Rectangle
    Area_A = (RecA[2] - RecA[0]) * (RecA[3] - RecA[1])
    Area_B = (RecB[2] - RecB[0]) * (RecB[3] - RecB[1])

    # IOU
    iou = Area_Inter / (Area_A + Area_B - Area_Inter)

    return iou


img = np.zeros((512, 512, 3), np.uint8) #构造了一个512*512的Numpy数组,同时分配了三个颜色空间,np.uint8保证元素的值在[0,255]之间,即BGR颜色空间的值域。
img.fill(255) #fill the background color

RecA = [50,50,300,300]
RecB = [60,60,320,320]

IOU = CountIOU(RecA,RecB)
print(IOU)

# draw rectangle
# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift )
cv2.rectangle(img, (RecA[0],RecA[1]), (RecA[2],RecA[3]), (0, 255, 0), 1)
cv2.rectangle(img, (RecB[0],RecB[1]), (RecB[2],RecB[3]), (255, 0, 0), 1)

IOU = CountIOU(RecA,RecB)
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,"IOU = %.2f"%IOU,(130, 190),font,0.8,(0,0,0),2)

# cv2.imshow("image",img)
cv2.imwrite("IoU.jpg", img)
# cv2.waitKey()
# cv2.destroyAllWindows()
