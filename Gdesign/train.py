#!/usr/bin/env
#coding:utf-8
'''''Train a simple convnet on the part olivetti faces dataset.

Run on GPU: THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python mnist_cnn.py

Get to 95% test accuracy after 25 epochs (there is still a lot of margin for parameter tuning).
'''

import numpy
numpy.random.seed(1337)  # for reproducibility

from PIL import Image

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
import codecs
import json
import time


def Net_model(nb_filters1,nb_filters2,nb_classes,nb_conv,img_rows,img_cols,nb_pool,lr=0.005, decay=1e-6, momentum=0.9):
    model = Sequential()
    model.add(Convolution2D(nb_filters1, nb_conv, nb_conv,
                            border_mode='valid',
                            input_shape=(img_rows, img_cols,1)))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))

    model.add(Convolution2D(nb_filters2, nb_conv, nb_conv))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    # model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1000))  # Full connection
    model.add(Activation('tanh'))
    # model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    sgd = SGD(lr=lr, decay=decay, momentum=momentum, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd)

    return model

def train(x,y):

    nb_classes=len(y)/10
    # There are 40 different classes
    # nb_classes = 41
    nb_epoch = 40
    batch_size = 40

    # input image dimensions
    img_rows, img_cols = 57, 47
    # number of convolutional filters to use
    nb_filters1, nb_filters2 = 5, 10
    # size of pooling area for max pooling
    nb_pool = 2
    # convolution kernel size
    nb_conv = 3


    x_train=x.reshape(x.shape[0],img_rows,img_cols,1)
    y_train=np_utils.to_categorical(y,nb_classes)


    model = Net_model(nb_filters1,nb_filters2,nb_classes,nb_conv,img_rows,img_cols,nb_pool)
    model.fit(x_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch, verbose=1)
    #保存现有的模型，保存两份。
    timeStamp=(long)(time.time())
    timeArray=time.localtime(timeStamp)
    TIME=time.strftime("%Y-%m-%d-%H:%M:%S",timeArray)
    # model.save('model/model.'+TIME+'.h5',overwrite=True)
    # model.save('model/model.h5',overwrite=True)
    model_json = model.to_json()
    with open("model/model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model/model.h5")
    print("Saved model to disk")
    # config = model.get_config()
    # with codecs.open('model/model.'+TIME+'.h5','w','utf-8') as f:
    #     json.dump(config,f)
    # with codecs.open('model/model.h5','w','utf-8') as f:
    #     json.dump(config,f)
    # return model

from getface import getface
if __name__=='__main__':
    x,y=getface()
    print train(x,y)

