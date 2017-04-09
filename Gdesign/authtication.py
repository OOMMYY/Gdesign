#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rece2base import rece2base
from getface import getface
from train import train
from auth_show import auth_show

def authtification():
    rece2base()
    x,y=getface()
    train(x,y)
    auth_show()


if __name__ == '__main__':
    authtification()
