#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image
import numpy as np


def xface(path):
    img=Image.open(path)
    img_array=np.asarray(img,dtype='float64')/255
    img_rows,img_cols = 57,47
    facedata=np.empty((img_rows*img_cols))
    facedata=np.ndarray.flatten(img_array)
    return facedata

if __name__=='__main__':
    facedata=xface(sys.argv[1])
    print facedata
    print facedata.shape
