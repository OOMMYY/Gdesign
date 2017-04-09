#coding:utf-8
#读取图片信息，然后转化为向量，先转化以A开头的人名
from PIL import Image
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import time

folder = listdir('lfw')
name = folder[1]
print name
picPath = listdir("lfw/"+name)[0]
print picPath


#读取图片，把图片转化为一个向量，返回所有图片向量的一个举证你n*1850
def getVec(picPath):
    VEC=[]
    for name in picPath:
        if name.endswith(".DS_Store"):
            continue
        vec = []
        img = Image.open(name)
        img = img.resize((50, 37), Image.ANTIALIAS)
        img = np.array(img)
        # Gray = (R*299 + G*587 + B*114 + 500) / 1000
        for col in img:
            for row in col:
                pix = (row[0] * 299 + row[1] * 587 + row[2] * 114 + 500) / 1000
                pix = pix/255.0
                vec.append(pix)
        VEC.append(vec)
    return VEC

path='lfw'
NAMES=listdir(path)
names=[]
for i in range(1,160):
    each=NAMES[i]
    names.append(each)
picPath=[]
aims=[]
for name in names:
    PICS=listdir(path+"/"+name)
    for pic in PICS:
        picPath.append(path+"/"+name+"/"+pic)
        aims.append(name)
print 'pic size:',len(picPath)
picVec=getVec(picPath)
print "vec size:",len(picVec),len(picVec[0])

n_components = 150
from sklearn.decomposition import PCA
pca = PCA(n_components=n_components, svd_solver='randomized',
          whiten=True).fit(picVec)

vec_pca=pca.transform(picVec)
print "pca size:",len(vec_pca),len(vec_pca[0])

#---------------------------------------------------
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced',probability=False), param_grid)
clf = clf.fit(vec_pca, np.array(aims))
print clf.score(vec_pca, np.array(aims))
print aims[4],clf.predict(np.array(vec_pca[4]).reshape(1,-1))
p=clf.decision_function(np.array(vec_pca[4]).reshape(1,-1))
print p[0][4]








