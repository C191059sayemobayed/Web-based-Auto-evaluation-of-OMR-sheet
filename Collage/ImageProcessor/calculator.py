
#from Collage.ImageProcessor import crop_ans
import numpy as np
import cv2
from Collage.ImageProcessor.crop_sheet import crop_sheet
import math
import  Collage.ImageProcessor.new_crop_ans as new_crop_ans

def meta_calculator(img):
    cnta = []
    crop_img = []

    tr = img
    br = np.array(img)
    ar = []

    mx = br.max()
    mn = br.min()
    #print(mx,mn)

    for i in range(388):
        for j in range(388):
    #       ar[i][j] = (1 if new_crop[i][j] < 110 else 255)
    #       new_crop[i][j] = (255 if new_crop[i][j]+80 > 255 else new_crop[i][j]+50)
            tr[i][j] = math.floor(((tr[i][j]-mn)/(mx-mn))*255.00)
            tr[i][j] = (0 if tr[i][j] < 80 else 255)



    #first_column_20-75

    ar.append(new_crop_ans.process_image_and_array(tr[20:40,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[45:60,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[65:80,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:100,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[105:120,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[120:136,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[137:154,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[155:172,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[173:192,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[193:210,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[300:316,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[317:335,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[336:352,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[353:370,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[371:387,22:71],cnta))

    #Second_column_95-150

    ar.append(new_crop_ans.process_image_and_array(tr[5:22,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[23:38,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[39:66,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[67:84,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:107,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[120:140,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[175:195,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:215,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:340,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:375,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,97:146],cnta))

    #Third_column_175-230

    ar.append(new_crop_ans.process_image_and_array(tr[22:40,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[41:58,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[59:85,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[86:103,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[104:119,180:229],cnta))


    ar.append(new_crop_ans.process_image_and_array(tr[120:136,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[137:154,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[155:172,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[173:189,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:208,180:229],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,180:229],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:335,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:370,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,180:229],cnta))

    #fourth_column_250-305

    ar.append(new_crop_ans.process_image_and_array(tr[5:22,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[23:38,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[39:66,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[67:84,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:107,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[100:120,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[120:140,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[180:200,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:335,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:370,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,255:304],cnta))

    #fifth_column_325-385

    ar.append(new_crop_ans.process_image_and_array(tr[5:25,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[25:45,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[45:70,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[65:85,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[80:105,331:380],cnta))


    ar.append(new_crop_ans.process_image_and_array(tr[120:140,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[175:195,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:215,331:380],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:245,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,331:380],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:316,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[317:332,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[333:348,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[349:367,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[368:385,331:380],cnta))




    
    return np.array(ar) , cnta




def crop_img_function():
    crop_img = []

    #for_first_column_20-75

    crop_img.append((20,40,20,75))
    crop_img.append((45,60,20,75))
    crop_img.append((65,80,20,75))
    crop_img.append((85,100,20,75))
    crop_img.append((105,120,20,75))

    crop_img.append((120,136,20,75))
    crop_img.append((137,154,20,75))
    crop_img.append((155,172,20,75))
    crop_img.append((173,192,20,75))
    crop_img.append((193,210,20,75))

    crop_img.append((210,230,20,75))
    crop_img.append((225,250,20,75))
    crop_img.append((245,265,20,75))
    crop_img.append((260,285,20,75))
    crop_img.append((280,300,20,75))

    crop_img.append((300,316,20,75))
    crop_img.append((317,335,20,75))
    crop_img.append((336,352,20,75))
    crop_img.append((353,370,20,75))
    crop_img.append((371,387,20,75))

    #Second_column_95-150

    crop_img.append((5,22,95,150))
    crop_img.append((23,38,95,150))
    crop_img.append((39,66,95,150))
    crop_img.append((67,84,95,150))
    crop_img.append((85,107,95,150))

    crop_img.append((120,140,95,150))
    crop_img.append((140,160,95,150))
    crop_img.append((160,180,95,150))
    crop_img.append((175,195,95,150))
    crop_img.append((190,215,95,150))

    crop_img.append((210,230,95,150))
    crop_img.append((225,250,95,150))
    crop_img.append((245,265,95,150))
    crop_img.append((260,285,95,150))
    crop_img.append((280,300,95,150))

    crop_img.append((295,320,95,150))
    crop_img.append((315,340,95,150))
    crop_img.append((335,355,95,150))
    crop_img.append((350,375,95,150))
    crop_img.append((370,388,95,150))

    #Third_column_175-230


    crop_img.append((22,40,175,230))
    crop_img.append((41,58,175,230))
    crop_img.append((59,85,175,230))
    crop_img.append((86,103,175,230))
    crop_img.append((104,119,175,230))


    crop_img.append((120,136,175,230))
    crop_img.append((137,154,175,230))
    crop_img.append((155,172,175,230))
    crop_img.append((173,189,175,230))
    crop_img.append((190,208,175,230))

    crop_img.append((210,230,175,230))
    crop_img.append((225,250,175,230))
    crop_img.append((245,265,175,230))
    crop_img.append((260,285,175,230))
    crop_img.append((280,300,175,230))

    crop_img.append((295,320,175,230))
    crop_img.append((315,335,175,230))
    crop_img.append((335,355,175,230))
    crop_img.append((350,370,175,230))
    crop_img.append((370,388,175,230))

    #fourth_column_250-305

    crop_img.append((5,22,250,305))
    crop_img.append((23,38,250,305))
    crop_img.append((39,66,250,305))
    crop_img.append((67,84,250,305))
    crop_img.append((85,107,250,305))

    crop_img.append((100,120,250,305))
    crop_img.append((120,140,250,305))
    crop_img.append((140,160,250,305))
    crop_img.append((160,180,250,305))
    crop_img.append((180,200,250,305))

    crop_img.append((210,230,250,305))
    crop_img.append((225,250,250,305))
    crop_img.append((245,265,250,305))
    crop_img.append((260,285,250,305))
    crop_img.append((280,300,250,305))

    crop_img.append((295,320,250,305))
    crop_img.append((315,335,250,305))
    crop_img.append((335,355,250,305))
    crop_img.append((350,370,250,305))
    crop_img.append((370,388,250,305))

    #fifth_column_325-385

    crop_img.append((5,25,325,385))
    crop_img.append((25,45,325,385))
    crop_img.append((45,70,325,385))
    crop_img.append((65,85,325,385))
    crop_img.append((80,105,325,385))


    crop_img.append((120,140,325,385))
    crop_img.append((140,160,325,385))
    crop_img.append((160,180,325,385))
    crop_img.append((175,195,325,385))
    crop_img.append((190,215,325,385))

    crop_img.append((210,230,325,385))
    crop_img.append((225,245,325,385))
    crop_img.append((245,265,325,385))
    crop_img.append((260,285,325,385))
    crop_img.append((280,300,325,385))

    crop_img.append((295,316,325,385))
    crop_img.append((317,332,325,385))
    crop_img.append((333,348,325,385))
    crop_img.append((349,367,325,385))
    crop_img.append((368,385,325,385))
    
    
    return crop_img



def mark_error(exam_sheet,ar,br,crop_img,cnt,x,y):
    
    img = cv2.cvtColor(exam_sheet, cv2.COLOR_GRAY2BGR)
    
    
    
    for i in range(0,100):
        if ar[i] in br[i]:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1],x+crop_img[i][2]+(ar[i]*12):x+crop_img[i][3]+(ar[i]*12 + 12)],cnt[i],-1,(0, 255, 0),4)
        else:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1],x+crop_img[i][2]+(ar[i]*12):x+crop_img[i][3]+(ar[i]*12 + 12)],cnt[i], -1, (0, 0, 255),4)

    
    
    return img



def new_process_test(img):

    new_crop = img
    
    br = []

    tr = new_crop.copy()
    k = np.array(new_crop)
    mx = k.max()
    mn = k.min()
    #print(mx,mn)


    for i in range(388):
        for j in range(388):
    #       ar[i][j] = (1 if new_crop[i][j] < 110 else 255)
    #       new_crop[i][j] = (255 if new_crop[i][j]+80 > 255 else new_crop[i][j]+50)
            tr[i][j] = math.floor(((tr[i][j]-mn)/(mx-mn))*255.00)
            tr[i][j] = (0 if tr[i][j] < 80 else 255)

    #first_column_20-75

    br.append(new_crop_ans.process_image_and_array_for_test(tr[20:40,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[45:60,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[65:80,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[85:100,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[105:120,22:71]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[120:136,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[137:154,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[155:172,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[173:192,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[193:210,22:71]))


    br.append(new_crop_ans.process_image_and_array_for_test(tr[210:230,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[225:250,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[245:265,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[260:285,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[280:300,22:71]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[300:316,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[317:335,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[336:352,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[353:370,22:71]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[371:387,22:71]))


    #Second_column_95-150

    br.append(new_crop_ans.process_image_and_array_for_test(tr[5:22,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[23:38,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[39:66,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[67:84,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[85:107,97:146]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[120:140,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[140:160,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[160:180,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[175:195,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[190:215,97:146]))


    br.append(new_crop_ans.process_image_and_array_for_test(tr[210:230,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[225:250,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[245:265,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[260:285,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[280:300,97:146]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[295:320,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[315:340,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[335:355,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[350:375,97:146]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[370:388,97:146]))

    #Third_column_175-230

    br.append(new_crop_ans.process_image_and_array_for_test(tr[22:40,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[41:58,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[59:85,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[86:103,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[104:119,180:229]))


    br.append(new_crop_ans.process_image_and_array_for_test(tr[120:136,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[137:154,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[155:172,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[173:189,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[190:208,180:229]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[210:230,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[225:250,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[245:265,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[260:285,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[280:300,180:229]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[295:320,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[315:335,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[335:355,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[350:370,180:229]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[370:388,180:229]))

    #fourth_column_250-305

    br.append(new_crop_ans.process_image_and_array_for_test(tr[5:22,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[23:38,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[39:66,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[67:84,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[85:107,255:304]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[100:120,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[120:140,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[140:160,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[160:180,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[180:200,255:304]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[210:230,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[225:250,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[245:265,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[260:285,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[280:300,255:304]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[295:320,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[315:335,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[335:355,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[350:370,255:304]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[370:388,255:304]))

    #fifth_column_325-385

    br.append(new_crop_ans.process_image_and_array_for_test(tr[5:25,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[25:45,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[45:70,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[65:85,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[80:105,331:380]))


    br.append(new_crop_ans.process_image_and_array_for_test(tr[120:140,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[140:160,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[160:180,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[175:195,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[190:215,331:380]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[210:230,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[225:245,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[245:265,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[260:285,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[280:300,331:380]))

    br.append(new_crop_ans.process_image_and_array_for_test(tr[295:316,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[317:332,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[333:348,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[349:367,331:380]))
    br.append(new_crop_ans.process_image_and_array_for_test(tr[368:385,331:380]))

    return br


        
def new_process(img,extra_info):
    x, y, w, h = extra_info
    
     
    new_crop = img

    cnta = []
    crop_img = []

    tr = new_crop.copy()
    br = np.array(new_crop)
    ar = []

    mx = br.max()
    mn = br.min()
    #print(mx,mn)

    for i in range(388):
        for j in range(388):
    #       ar[i][j] = (1 if new_crop[i][j] < 110 else 255)
    #       new_crop[i][j] = (255 if new_crop[i][j]+80 > 255 else new_crop[i][j]+50)
            tr[i][j] = math.floor(((tr[i][j]-mn)/(mx-mn))*255.00)
            tr[i][j] = (0 if tr[i][j] < 80 else 255)



    #first_column_20-75

    ar.append(new_crop_ans.process_image_and_array(tr[20:40,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[45:60,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[65:80,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:100,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[105:120,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[120:136,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[137:154,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[155:172,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[173:192,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[193:210,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,22:71],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[300:316,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[317:335,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[336:352,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[353:370,22:71],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[371:387,22:71],cnta))

    #Second_column_95-150

    ar.append(new_crop_ans.process_image_and_array(tr[5:22,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[23:38,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[39:66,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[67:84,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:107,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[120:140,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[175:195,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:215,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,97:146],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:340,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:375,97:146],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,97:146],cnta))

    #Third_column_175-230

    ar.append(new_crop_ans.process_image_and_array(tr[22:40,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[41:58,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[59:85,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[86:103,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[104:119,180:229],cnta))


    ar.append(new_crop_ans.process_image_and_array(tr[120:136,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[137:154,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[155:172,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[173:189,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:208,180:229],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,180:229],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:335,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:370,180:229],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,180:229],cnta))

    #fourth_column_250-305

    ar.append(new_crop_ans.process_image_and_array(tr[5:22,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[23:38,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[39:66,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[67:84,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[85:107,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[100:120,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[120:140,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[180:200,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:250,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,255:304],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:320,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[315:335,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[335:355,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[350:370,255:304],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[370:388,255:304],cnta))

    #fifth_column_325-385

    ar.append(new_crop_ans.process_image_and_array(tr[5:25,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[25:45,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[45:70,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[65:85,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[80:105,331:380],cnta))


    ar.append(new_crop_ans.process_image_and_array(tr[120:140,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[140:160,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[160:180,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[175:195,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[190:215,331:380],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[210:230,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[225:245,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[245:265,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[260:285,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[280:300,331:380],cnta))

    ar.append(new_crop_ans.process_image_and_array(tr[295:316,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[317:332,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[333:348,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[349:367,331:380],cnta))
    ar.append(new_crop_ans.process_image_and_array(tr[368:385,331:380],cnta))





    #for_first_column_20-75

    crop_img.append((20,40,22,71))
    crop_img.append((45,60,22,71))
    crop_img.append((65,80,22,71))
    crop_img.append((85,100,22,71))
    crop_img.append((105,120,22,71))

    crop_img.append((120,136,22,71))
    crop_img.append((137,154,22,71))
    crop_img.append((155,172,22,71))
    crop_img.append((173,192,22,71))
    crop_img.append((193,210,22,71))

    crop_img.append((210,230,22,71))
    crop_img.append((225,250,22,71))
    crop_img.append((245,265,22,71))
    crop_img.append((260,285,22,71))
    crop_img.append((280,300,22,71))

    crop_img.append((300,316,22,71))
    crop_img.append((317,335,22,71))
    crop_img.append((336,352,22,71))
    crop_img.append((353,370,22,71))
    crop_img.append((371,387,22,71))

    #Second_column_95-150

    crop_img.append((5,22,97,146))
    crop_img.append((23,38,97,146))
    crop_img.append((39,66,97,146))
    crop_img.append((67,84,97,146))
    crop_img.append((85,107,97,146))

    crop_img.append((120,140,97,146))
    crop_img.append((140,160,97,146))
    crop_img.append((160,180,97,146))
    crop_img.append((175,195,97,146))
    crop_img.append((190,215,97,146))

    crop_img.append((210,230,97,146))
    crop_img.append((225,250,97,146))
    crop_img.append((245,265,97,146))
    crop_img.append((260,285,97,146))
    crop_img.append((280,300,97,146))

    crop_img.append((295,320,97,146))
    crop_img.append((315,340,97,146))
    crop_img.append((335,355,97,146))
    crop_img.append((350,375,97,146))
    crop_img.append((370,388,97,146))

    #Third_column_175-230


    crop_img.append((22,40,180,229))
    crop_img.append((41,58,180,229))
    crop_img.append((59,85,180,229))
    crop_img.append((86,103,180,229))
    crop_img.append((104,119,180,229))


    crop_img.append((120,136,180,229))
    crop_img.append((137,154,180,229))
    crop_img.append((155,172,180,229))
    crop_img.append((173,189,180,229))
    crop_img.append((190,208,180,229))

    crop_img.append((210,230,180,229))
    crop_img.append((225,250,180,229))
    crop_img.append((245,265,180,229))
    crop_img.append((260,285,180,229))
    crop_img.append((280,300,180,229))

    crop_img.append((295,320,180,229))
    crop_img.append((315,335,180,229))
    crop_img.append((335,355,180,229))
    crop_img.append((350,370,180,229))
    crop_img.append((370,388,180,229))

    #fourth_column_250-305

    crop_img.append((5,22,255,304))
    crop_img.append((23,38,255,304))
    crop_img.append((39,66,255,304))
    crop_img.append((67,84,255,304))
    crop_img.append((85,107,255,304))

    crop_img.append((100,120,255,304))
    crop_img.append((120,140,255,304))
    crop_img.append((140,160,255,304))
    crop_img.append((160,180,255,304))
    crop_img.append((180,200,255,304))

    crop_img.append((210,230,255,304))
    crop_img.append((225,250,255,304))
    crop_img.append((245,265,255,304))
    crop_img.append((260,285,255,304))
    crop_img.append((280,300,255,304))

    crop_img.append((295,320,255,304))
    crop_img.append((315,335,255,304))
    crop_img.append((335,355,255,304))
    crop_img.append((350,370,255,304))
    crop_img.append((370,388,255,304))

    #fifth_column_325-385

    crop_img.append((5,25,331,380))
    crop_img.append((25,45,331,380))
    crop_img.append((45,70,331,380))
    crop_img.append((65,85,331,380))
    crop_img.append((80,105,331,380))


    crop_img.append((120,140,331,380))
    crop_img.append((140,160,331,380))
    crop_img.append((160,180,331,380))
    crop_img.append((175,195,331,380))
    crop_img.append((190,215,331,380))

    crop_img.append((210,230,331,380))
    crop_img.append((225,245,331,380))
    crop_img.append((245,265,331,380))
    crop_img.append((260,285,331,380))
    crop_img.append((280,300,331,380))

    crop_img.append((295,316,331,380))
    crop_img.append((317,332,331,380))
    crop_img.append((333,348,331,380))
    crop_img.append((349,367,331,380))
    crop_img.append((368,385,331,380))

    for i in range(100):
        cv2.drawContours(new_crop[y + crop_img[i][0]:y + crop_img[i][1],x + crop_img[i][2] + (ar[i] * 12):x + crop_img[i][3] + (ar[i] * 12 + 12)], cnta[i], -1,(0, 255, 0), 4)

    return ar , crop_img, cnta
    
    
    
    
    
    
    
def calculate_imgage(ans_sheet,exam_sheet):
    
    # print(ans_sheet)
    ans_sheet, extra_info = crop_sheet(ans_sheet,True)
    exam_sheet = crop_sheet(exam_sheet)
    

    x, y, w, h = extra_info
    
    ar ,crop_img, cnt = new_process(ans_sheet,extra_info)      #TEMPLATE
    br  = new_process_test(exam_sheet)
    

    img = cv2.cvtColor(ans_sheet, cv2.COLOR_GRAY2BGR)
    for i in range(0,100):
        if ar[i] in br[i]:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1],x+crop_img[i][2]+(ar[i]*12):x+crop_img[i][3]+(ar[i]*12 + 12)],cnt[i],-1,(0, 255, 0),4)
        else:
            cv2.drawContours(img[y+crop_img[i][0]:y+crop_img[i][1],x+crop_img[i][2]+(ar[i]*12):x+crop_img[i][3]+(ar[i]*12 + 12)],cnt[i], -1, (0, 0, 255),4)

    chemistry = 0
    physics = 0
    math = 0
    english = 0
    analytical = 0
    
    for i in range(0,25):
        physics +=  (ar[i] in br[i])


    for i in range(25,40):
        chemistry +=  (ar[i] in br[i])

    for i in range(40, 70):
        math += (ar[i] in br[i])

    for i in range(70, 85):
        english += (ar[i] in br[i])

    for i in range(85, 100):
        analytical += (ar[i] in br[i])

        
        
    
    
    return {
        "physics":int(physics),
        "chemistry":int(chemistry),
        "math":int(math),
        "english":int(english),
        "analytical":int(analytical),
    } , img

