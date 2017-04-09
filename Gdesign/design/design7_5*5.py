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
        for each in PicName[:5]:
            vec=img2vec(Path+"/"+name+"/"+each)
            Vec.append(vec)
            aim.append(name)
    logger.debug("getPic()获取Vec done")
    return Vec,aim

Vec,aim=getPic()
Vec=vec2pca(Vec,150)
test=Vec[-5:]
testaim=aim[-5:]
aim=aim[:-5]
print json.dumps(aim)
Vec = Vec[:-5]
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
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced',decision_function_shape='ovr'), param_grid)
clf = clf.fit(Vec, np.array(aim))


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
#print(classification_report(test, testaim, target_names=[2]*5))
#print(confusion_matrix(test, testaim, labels=range(8)))

for each in test:
    p=clf.decision_function(np.array(each).reshape(1,-1))[0]
    #p=clf.predict_proba(np.array(each).reshape(1,-1))
    print p.tolist()
    print clf.predict(np.array(each).reshape(1,-1)),len(p)



#发现不能正确预测，改进方法，加入1000个单人照片，帮助训练。
# pca size: 45 45
# 40
# 45
# ['Adrien_Brody']
# ['Al_Sharpton']
# ['Alan_Greenspan']
# ['Ahmed_Chalabi']
# ['Ahmed_Chalabi']
#
# pca size: 45 45
# 40
# 45
# [-0.5         0.78006067  6.28695485  3.00692927  5.18856245  4.14715504
#   1.79006401  7.30027371]
# ['Abdullah_Gul'] 8
# [-0.5         0.78006067  6.28695485  3.00692927  5.18856245  4.14715504
#   1.79006401  7.30027371]
# ['Albert_Costa'] 8
# [-0.5         0.78006067  6.28695485  3.00692927  5.18856245  4.14715504
#   1.79006401  7.30027371]
# ['Albert_Costa'] 8
# [-0.5         0.78006067  6.28695485  3.00692927  5.18856245  4.14715504
#   1.79006401  7.30027371]
# ['Al_Gore'] 8
# [-0.5         0.78006067  6.28695485  3.00692927  5.18856245  4.14715504
#   1.79006401  7.30027371]
# ['Ai_Sugiyama'] 8
