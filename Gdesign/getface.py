#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import cPickle
from os import listdir
import numpy as np
from xface import xface
import json
import codecs

def getface():
    with open('model/olivettifaces.pkl','rb') as f:
        oliverface,oliverlabel=cPickle.load(f)
    #从base中读入人脸数据
    source='image/base/'
    foders=listdir(source)
    pic=[]
    label=[]
    dic={}
    for i in range(len(foders)):
        foder=foders[i]
        names=listdir(source+foder)
        dic[str(40+i)]=foder
        for name in names:
            path =source+foder+'/'+name
            pic.append(path)
            label.append(40+i)
    with codecs.open('conf/NameMap.cnf','w','utf-8') as f:
        json.dump(dic,f,ensure_ascii=False)
    n=len(pic)
    length=57*47
    baseface=np.empty((n,length))
    baselabel=np.asarray(label)
    for i in range(n):
        baseface[i]=xface(pic[i])
    return np.concatenate((oliverface,baseface),axis=0),np.concatenate((oliverlabel,baselabel),axis=0)


if __name__=='__main__':
    faces,labels=getface()
    print 'face shape:',faces.shape
    print 'label shape:',labels.shape
