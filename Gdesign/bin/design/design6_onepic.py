#coding:utf-8
#1.训练集取150个人每人一张图片，训练模型加入刘德华的照片，然后预测刘德华的另一张照片
#2.增加刘德华，刘亦菲的的数量，再次训练上述模型
from PIL import Image
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import logging
from logging.config import fileConfig
from os import listdir

fileConfig('logging_conf.ini')
logger=logging.getLogger()

def getMyVec(picPath):
    img = Image.open(picPath)
    img=img.resize((50,37),Image.ANTIALIAS)
    img = np.asarray(img)
    vec=[]
    for col in img:
        for row in col:
            pix = (row[0] * 299 + row[1] * 587 + row[2] * 114 + 500) / 1000
            pix = pix / 255.0
            vec.append(pix)
    return vec
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
from os import listdir
def getTrainVec():
    path = 'lfw'
    NAMES = listdir(path)
    names = []
    for i in range(1, 1000):
        each = NAMES[i]
        names.append(each)
    picPath = []
    aims = []
    for name in names:
        PICS = listdir(path + "/" + name)
        for pic in PICS:
            picPath.append(path + "/" + name + "/" + pic)
            aims.append(name)
    print 'pic size:', len(picPath)
    picVec = getVec(picPath)
    print "vec size:", len(picVec), len(picVec[0])
    return  picVec,aims

def getPCA(picVec):
    n_components = 150
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components, svd_solver='randomized',
              whiten=True).fit(np.array(picVec))
    vec_pca = pca.transform(np.array(picVec))
    print "pca size:", len(vec_pca), len(vec_pca[0])
    return vec_pca

#获得150张不同人的照片向量
def getPic(img_num):
    Path='/Users/liuyuanzhen/ImageBase/lfw'

    NAMES=listdir(Path)
    Vec=[]
    aim=[]
    for i in range(img_num):
        name=NAMES[i]
        PicName=listdir(Path+"/"+name)[0]
        vec=getMyVec(Path+"/"+name+"/"+PicName)
        Vec.append(vec)
        aim.append(name)
    logger.debug("getPic()获取Vec done")
    return Vec,aim

Vec,aim=getPic(150)
vec_train=getMyVec('Aaron_Peirsol_0001.jpg')
vec_test=getMyVec('Aaron_Peirsol_0001.jpg')
Vec = Vec+[vec_train,vec_test]
aim =aim+['liudehua']
print len(Vec)
print len(Vec[0])
Vec=getPCA(Vec)
vec_test=Vec[-1]
Vec=Vec[:-1]

# print len(Vec)
# for each in aim:
#     print each
# print len(aim)
# exit()
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

clf=SVC()
clf = clf.fit(Vec, np.array(aim))

print clf.predict(np.array(vec_test).reshape(1,-1))
p=clf.decision_function(np.array(vec_test).reshape(1,-1))
for each in p[0]:
    print each,
print
print p[0][-1]
exit()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced',probability=False), param_grid)
clf = clf.fit(Vec, np.array(aim))
print clf.predict(np.array(vec_test).reshape(1,-1))
p=clf.decision_function(np.array(vec_test).reshape(1,-1))


#制作5V5识别程序

