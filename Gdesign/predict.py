#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from keras.models import load_model
from keras.models import model_from_json
import numpy as np
import  tensorflow as tf
np.random.seed(1337)
import json
import codecs
from keras.optimizers import SGD

import tensorflow as tf
import numpy as np

class ImageAugmenter(object):
    def __init__(self, sess):
        self.sess = sess
        self.im_placeholder = tf.placeholder(tf.float32, shape=[1,784,3])

    def augment(self, image):
        augment_op = tf.image.random_saturation(self.im_placeholder, 0.6, 0.8)
        return self.sess.run(augment_op, {self.im_placeholder: image})

class DataFeed(object):
    def __init__(self, data_dir, sess):
        self.images = load_data(data_dir)
        self.augmenter = ImageAugmenter(sess)

    def process_data(self):
        processed_images = []
        for im in self.images:
            processed_images.append(self.augmenter.augment(im))
        return processed_images

def load_data(data_dir):
    # True method would read images from disk
    # This is just a mockup
    images = []
    images.append(np.random.random([1,784,3]))
    images.append(np.random.random([1,784,3]))
    return images

def predict(x):
    x_predict=np.empty((1,len(x)))
    x_predict[0]=x
    x_predict=x_predict.reshape(x_predict.shape[0],57,47,1)
    # load json and create model
    json_file = open('model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model/model.h5")
    print("Loaded model from disk")
    # model=load_model('model/model.h5')
    # lr = 0.005
    # decay = 1e-6
    # momentum = 0.9
    # sgd = SGD(lr=lr, decay=decay, momentum=momentum, nesterov=True)
    # model.compile(loss='categorical_crossentropy', optimizer=sgd)
    #config = json.load(codecs.open('model/model.h5','r','utf-8'),'utf-8')
    # print config
    # model = Sequential.from_config(config)

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
    TRAIN_DATA_DIR = '/some/dir/'
    sess = tf.Session()
    data_feed = DataFeed(TRAIN_DATA_DIR, sess)
    train_data = data_feed.process_data()
    print(train_data)


