#coding:utf-8
##制作5V5识别程序,最后五张图片为测试图片
#程序识别效果特别差，没有准确度，使用decision_function查看用例与超平面之间的距离，发现也并没有用。
#design8从图片库中每人取一张照片，继续训练

from PIL import Image
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import logging
from logging.config import fileConfig
from os import listdir
import json
import pprint

fileConfig('logging_conf.ini')
logger=logging.getLogger()


from os import listdir
from autil import img2vec,vec2pca
import os

#获得5*5中的照片向量
def getPic():
    Path='/Users/liuyuanzhen/ImageBase/5*5'
    if os.path.isfile(Path+"/.DS_Store"):
        os.remove(Path+"/.DS_Store")
    NAMES=listdir(Path)
    Vec=[]
    aim=[]
    for i in range(len(NAMES)):
        name=NAMES[i]
        if os.path.isfile(Path+"/"+name+"/.DS_Store"):
           os.remove(Path+"/"+name+"/.DS_Store")
        PicName=listdir(Path+"/"+name)
        for each in PicName[1:2]:
            vec=img2vec(Path+"/"+name+"/"+each)
            Vec.append(vec)
            aim.append(name)
    logger.debug("getPic()获取Vec done")
    return Vec,aim

def getPerson(n):
    Path = '/Users/liuyuanzhen/ImageBase/5*5'
    if os.path.isfile(Path + "/.DS_Store"):
        os.remove(Path + "/.DS_Store")
    NAMES = listdir(Path)
    Vec = []
    aim = []
    for i in range(n):
        name = NAMES[i]
        if os.path.isfile(Path + "/" + name + "/.DS_Store"):
            os.remove(Path + "/" + name + "/.DS_Store")
        PicName = listdir(Path + "/" + name)[0]
        vec = img2vec(Path + "/" + name + "/" + PicName)
        Vec.append(vec)
        aim.append(name)
    logger.debug("getPerson("+str(n)+")获取Vec done")
    return Vec,aim

Vec,aim=getPic()
people,paim=getPerson(10)
Vec= people+Vec
aim=paim+aim
n=10
#Vec=vec2pca(Vec,150)
test=Vec[-n:]
testaim=aim[-n:]
aim=aim[:-n]
print json.dumps(aim)
Vec = Vec[:-n]
print len(Vec)
print len(Vec[0])


# print len(Vec)
# for each in aim:
#     print each
# print len(aim)
# exit()
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
#clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced',decision_function_shape='ovo'), param_grid)
clf =SVC(kernel='rbf', class_weight='balanced',decision_function_shape='ovo')
clf = clf.fit(Vec, np.array(aim))


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
#print(classification_report(test, testaim, target_names=[2]*5))
#print(confusion_matrix(test, testaim, labels=range(8)))

for each in test:
    #p=clf.decision_function(np.array(each).reshape(1,-1))[0]
    #p=clf.predict_proba(np.array(each).reshape(1,-1))
    #print p.tolist()
    print clf.predict(np.array(each).reshape(1,-1))

