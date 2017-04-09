#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from cutface import cutface
from xface import xface

def getPredict():
    source='image/img_predict/predict.jpg'
    target='image/img_predict/minPredict.jpg'
    cutface(source,target)
    return xface(target)
if __name__=='__main__':
    face=getPredict()
    print face.shape

