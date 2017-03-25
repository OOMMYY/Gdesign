#coding:utf-8
#训练模型加入刘德华的照片，然后预测刘德华的另一张照片
from PIL import Image
import numpy as np
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
    path = '/Users/liuyuanzhen/ImageBase/lfw'
    NAMES = listdir(path)
    names = []
    for i in range(1, 100):
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
              whiten=True).fit(picVec)
    vec_pca = pca.transform(picVec)
    print "pca size:", len(vec_pca), len(vec_pca[0])
    return vec_pca

mytrain=getMyVec('lujiaqi01.jpg')
myaim=getMyVec('lujiaqi02.jpg')

train,aims=getTrainVec()
train.append(mytrain)
train.append(myaim)
aims.append("lujiaqi")
pca = getPCA(train)
myaim=pca[-1]
pca=pca[:-1]


from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced',probability=False), param_grid)
clf = clf.fit(pca, np.array(aims))
print clf.predict(np.array(myaim).reshape(1,-1))
p=clf.decision_function(np.array(myaim).reshape(1,-1))
print p
print p[0][4]
