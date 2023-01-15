import PIL
import cv2
import numpy as np

flyer = cv2.imread(r'/Users/shrutianand/Documents/daisy 2023/flyer3.png')

img = cv2.Canny(flyer, 50, 150)
kernel = np.ones((5, 5))
img_dilation = cv2.dilate(img, kernel)

contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for i in range(len(contours)):
    if hierarchy[0][i][2] == -1:
        continue

    if cv2.contourArea(contours[i]) > 7000:
       # cv2.drawContours(img, contours=[contours[i]], contourIdx=-1, color=(255,0,255), thickness=1, lineType=cv2.LINE_AA)
    
        contour_approx_flat = list(np.array(contours[i]).flatten())

        contour_xs = [contour_approx_flat[j] for j in range(len(contour_approx_flat)) if j % 2 == 0]
        contour_ys = [contour_approx_flat[j] for j in range(len(contour_approx_flat)) if j % 2 == 1]

        contour_xs.sort()
        contour_ys.sort()
        
        cropped= flyer[contour_ys[0]:contour_ys[-1], contour_xs[0]:contour_xs[-1]]
        
        cv2.imwrite(r"/Users/shrutianand/Documents/daisy 2023/ad_" + str(i) +".png", cropped)


cv2.imshow("None approximation", img)
cv2.waitKey(0)