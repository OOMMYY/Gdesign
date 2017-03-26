#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation,Flatten
from keras.layers.convolutional import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import time

def train(x,y):
    batch_size=10
    nb_classes=len(y)/10
    nb_epoch=12
    img_rows,img_cols=57,47
    nb_filters=32
    nb_pool=2
    nb_conv=3
    x_train=x.reshape(x.shape[0],img_rows,img_cols,1)
    y_train=np_utils.to_categorical(y,nb_classes)
   
    model=Sequential()
    model.add(Convolution2D(nb_filters, nb_conv, nb_conv,border_mode='valid',input_shape=(img_rows, img_cols,1)))
    model.add(Activation('relu'))
    model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adadelta',metrics=['accuracy'])

    model.fit(x_train,y_train,batch_size=batch_size,nb_epoch=nb_epoch,verbose=1,validation_split=0.0, validation_data=None)
    #保存现有的模型，保存两份。
    timeStamp=(long)(time.time())
    timeArray=time.localtime(timeStamp)
    TIME=time.strftime("%Y-%m-%d-%H:%M:%S",timeArray)
    model.save('../model/model.'+TIME+'.h5')
    model.save('../model/model.h5')
    return model

from getface import getface
if __name__=='__main__':
    x,y=getface()
    print train(x,y)

