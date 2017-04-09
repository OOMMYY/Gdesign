#!/usr/bin/env
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json

def veri_show(x,prob):
    print x,prob
    if x < 40 or prob < 0.5:
        return  "不能识别",prob
    else:
    	dic=json.load(open('conf/NameMap.cnf','r'),'utf-8')
    	name=dic[str(x).strip()]
        return  name,prob

if __name__=='__main__':
    pass

