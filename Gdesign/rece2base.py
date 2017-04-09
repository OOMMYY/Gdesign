#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from os import listdir
import shutil
from cutface import cutface

#入库前先清除原有数据
def rece2base():
    source='image/img_receive'
    name='received'
    names=listdir(source)
    if len(names)<10:
        return False
    name=names[0].encode('utf-8').split('_')[0]
    target='image/base/'+name
    if os.path.exists(target):
        shutil.rmtree(target)
    os.makedirs(target)
    source+='/'
    target+='/'
    for each in names:
        each =each.encode('utf-8')
        cutface(source+each,target+each)
    return True

if __name__=='__main__':
   print  rece2base()
