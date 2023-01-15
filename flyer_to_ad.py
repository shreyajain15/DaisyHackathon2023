import PIL
import cv2
import numpy as np
import os

flyer = cv2.imread(os.getcwd() + 'freshco_flyer_4.png')

img = cv2.Canny(flyer, 50, 150)

contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
#print(contours)
""" high_blurred = cv2.GaussianBlur(flyer, (333,333), 0)
mean_sub = cv2.subtract(flyer, high_blurred)

blurred = cv2.GaussianBlur(grey, (21,21), 0)

thresh, thresh_img = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("image", thresh_img) """

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for i in range(len(contours)):
    if hierarchy[0][i][2] == -1:
        continue

    if cv2.contourArea(contours[i]) > 0:
       cv2.drawContours(img, contours=[contours[i]], contourIdx=-1, color=(255,0,255), thickness=1, lineType=cv2.LINE_AA)
       contour_approx_flat = list(np.array(contours[i]).flatten())
       contour_xs = [contour_approx_flat[j] for j in range(len(contour_approx_flat)) if j % 2 == 0]
       contour_ys = [contour_approx_flat[j] for j in range(len(contour_approx_flat)) if j % 2 == 1]
       contour_xs.sort()
       contour_ys.sort()
        
       cropped= flyer[contour_ys[0]:contour_ys[-1], contour_xs[0]:contour_xs[-1]]
       
       cv2.imwrite(os.getcwd() + str(i) +".png", cropped)

    # contour_approx = cv2.approxPolyDP(contours[i], 0.05* cv2.arcLength(contours[i], True), True)
    # cv2.drawContours(img, contours=[contours[i]], contourIdx=-1, color=(255,0,255), thickness=1, lineType=cv2.LINE_AA)
    # if len(contour_approx_flat) == 8:
    #     print(contour_approx_flat, "allalala")

cv2.imshow("None approximation", img)
cv2.waitKey(0)
