#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image
import numpy as np
import logging
from logging.config import fileConfig


fileConfig('logging_conf.ini')
logger=logging.getLogger()
#logger.debug("test %s","visiting")


def hello():
    print "hello"


def img2vec(picPath):
    img = Image.open(picPath)
    img = img.resize((50, 37), Image.ANTIALIAS)
    img = np.asarray(img)
    vec = []
    for col in img:
        for row in col:
            pix = (row[0] * 299 + row[1] * 587 + row[2] * 114 + 500) / 1000
            pix = pix / 255.0
            vec.append(pix)
    return vec

from sklearn.decomposition import PCA
def vec2pca(Vec,n_components):
    pca = PCA(n_components=n_components, svd_solver='randomized',
              whiten=True).fit(np.array(Vec))
    vec_pca = pca.transform(np.array(Vec))
    print "pca size:", len(vec_pca), len(vec_pca[0])
    return vec_pca