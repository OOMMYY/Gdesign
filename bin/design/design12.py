#coding:utf-8
from __future__ import print_function
import numpy as np
import cPickle
from keras.models import load_model

np.random.seed(1337)  # for reproducibililty

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

# split data into train,vavlid and test
# train:320
# valid:40
# test:40


def split_data(fname):
    f = open(fname, 'rb')
    face_data, face_label = cPickle.load(f)

    X_train = np.empty((320, img_rows * img_cols))
    Y_train = np.empty(320, dtype=int)

    X_valid = np.empty((40, img_rows * img_cols))
    Y_valid = np.empty(40, dtype=int)

    X_test = np.empty((40, img_rows * img_cols))
    Y_test = np.empty(40, dtype=int)

    for i in range(40):
        X_train[i * 8:(i + 1) * 8, :] = face_data[i * 10:i * 10 + 8, :]
        Y_train[i * 8:(i + 1) * 8] = face_label[i * 10:i * 10 + 8]

        X_valid[i] = face_data[i * 10 + 8, :]
        Y_valid[i] = face_label[i * 10 + 8]

        X_test[i] = face_data[i * 10 + 9, :]
        Y_test[i] = face_label[i * 10 + 9]

    return (X_train, Y_train, X_valid, Y_valid, X_test, Y_test)

img_rows, img_cols = 57, 47
nb_classes = 40
(X_train, Y_train, X_valid, Y_valid, X_test, Y_test) = split_data('olivettifaces.pkl')
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols,1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols,1)
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
# convert label to binary class matrix
Y_train = np_utils.to_categorical(Y_train, nb_classes)
Y_test = np_utils.to_categorical(Y_test, nb_classes)

model=load_model('model11.h5')
score = model.evaluate(X_test, Y_test,  verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
#print(model.summary())


print (model.evaluate(X_test, Y_test,  verbose=0))
print (model.predict(X_test[:2]))
cla = model.predict_classes(X_test)
prob=model.predict_proba(X_test)
print ('-------')
for i in range(40):
    if cla[i]!=i:
        continue
        print (i,cla[i])
        print (prob[i])
    else:
        print (prob[i][i],)