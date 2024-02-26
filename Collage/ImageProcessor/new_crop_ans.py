import cv2
import numpy as np
import imutils
from imutils import contours


def process_image_and_array_for_test(img):
   # cv2.imshow("im3",image)
    ans = []




    for i in range(4):
        thresh = cv2.threshold(img[:,i*12:i*12 + 12], 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        array = []
       # cv2.imshow("img", img[:, i * 12:i * 12 + 12])
       # cv2.waitKey(0)


        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if (w>=6 and h>=6 and ar>=.6 and ar<= 2 and w<15 and h<15):
               ans.append(i)
            #   print(i)
               break
              # cv2.imshow("img2", img[:, i * 12:i * 12 + 12])
              # cv2.waitKey(0)

    ans.append(5)
    return ans

def process_image_and_array(img,cnta):
    ans = 0

    for i in range(4):
        thresh = cv2.threshold(img[:, i * 12:i * 12 + 12], 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        array = []

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if (w>=6 and h>=6 and ar>=.6 and ar<= 2 and w<15 and h<15):
                ans = i
             #   print(i)
                cnta.append(c)
                i = 5
    return ans