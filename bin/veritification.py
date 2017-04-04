#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from getPredict import getPredict
from predict import predict
from veri_show import veri_show

def veritification():
    x=getPredict()
    y,prob = predict(x)
    veri_show(y,prob)

if __name__=='__main__':
    veritification()
