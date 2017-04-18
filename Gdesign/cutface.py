#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import cv
from PIL import Image
import PIL.ExifTags as ExifTags

def cutface(source,target):
    img = Image.open(source)
    exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
    if 'Orientation' in exif :
        tag =(int)(exif['Orientation'])
        print tag,'Orientation'
        if tag == 5 or tag == 6:
            img = img.rotate(-90 , expand = True)
        if tag == 3 or tag == 4:
            img = img.rotate(180 , expand = True)
        if tag == 7 or tag == 8:
            img = img.rotate(90 , expand = True)
    #img = img.resize((96,128),Image.ANTIALIAS)
    img.save('static/images/tmp.jpeg')
    img = cv.LoadImage('static/images/tmp.jpeg');
    img=cv.LoadImage('static/images/tmp.jpeg')
    image_size=cv.GetSize(img)
    greyscale=cv.CreateImage(image_size,8,1)
    cv.CvtColor(img,greyscale,cv.CV_BGR2GRAY)
    storage=cv.CreateMemStorage(0)
    cv.EqualizeHist(greyscale,greyscale)
    cascade = cv.Load('conf/haarcascade_frontalface_alt2.xml')
    #faces=cv.HaarDetectObjects(greyscale, cascade, storage, 1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING,(50, 50))
    faces=cv.HaarDetectObjects(greyscale, cascade, storage, 1.1,3,0,(50, 50))
    if len(faces) == 0:
        return
    (x,y,w,h),n=faces[len(faces)-1]
    cv.SetImageROI(greyscale,(x,y,w,h))
    minimg=cv.CreateImage((57,47),8,1)
    cv.Resize(greyscale,minimg)
    cv.SaveImage(target,minimg)

if __name__=='__main__':
    cutface(sys.argv[1],sys.argv[2])
