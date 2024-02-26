import cv2
import imutils
from imutils import contours
from Collage.ImageProcessor import four_point 

def crop_sheet(image,extra=False):
    #answer_img
    image= image

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(750,900))
    edged = cv2.Canny(gray, 20, 200)
    cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None


    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if (len(approx) == 4):
                docCnt = approx
                break

    # find the four point of a page ...here use four_point.py file
    paper = four_point.four_point_transform(image, docCnt.reshape(4, 2))
    warped = four_point.four_point_transform(gray, docCnt.reshape(4, 2))

    #cv2.imshow("img3",warped)
    th2 =  cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    thresh = cv2.threshold(th2, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = max(cnts, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(cnts)
    crop = warped[y:y+h, x:x+w]
    crop = cv2.resize(crop,(388,388))
    new_crop = crop.copy()

    
    if extra:
        return new_crop, [ x, y, w, h]
    
    
    return new_crop