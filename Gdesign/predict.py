#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from keras.models import load_model
import numpy as np
np.random.seed(1337)

def predict(x):
    x_predict=np.empty((1,len(x)))
    x_predict[0]=x
    x_predict=x_predict.reshape(x_predict.shape[0],57,47,1)
    model=load_model('../model/model.h5') 
    cla=model.predict_classes(x_predict)
    prob=model.predict_proba(x_predict)
    cla=cla[0]
    prob=prob[0][cla]
    return cla,prob

from getPredict import getPredict
if __name__=='__main__':
    x=getPredict()
    cla ,prob = predict(x)
    print cla,prob


