#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from PIL import Image
import os
import shutil
from cutface import cutface
from authtication import authtification
import tensorflow as tf
import traceback
def menu(request):
    print "menu"
    return render(request,"backend.html",{})

def preview(request):
    print "preview"
    data = {}
    if request.POST:
        data['name'] = request.POST['test'].strip()
        files = request.FILES.getlist('files')
        target = 'image/img_receive'
        if os.path.exists(target):
            shutil.rmtree(target)
        os.makedirs(target)
        img_list = []
        count = 0
        for file in files:
            count += 1
            path = target +'/'+ data['name'] + '_' + str(count) + '.jpg'
            img = Image.open(file)
            img.save(path)
            img_list.append(path)
        #截图
        target = 'static/images/preview'
        if os.path.exists(target):
            shutil.rmtree(target)
        os.makedirs(target)
        count = 0
        preview_list = []
        for each in img_list:
            count += 1
            path = target+'/'+data['name']+'_'+str(count)+'.jpg'
            cutface(each,path)
            preview_list.append(path)
        #返回预览图
        data['preview'] = preview_list
    else:
        print "NOT POST"
    return render(request,"backend.html",data)

def auth(request):
    print "auth"
    data = {}
    try:
        with tf.Session():
            authtification()
        s = "认证成功。"
    except:
        s = "认证失败!<br>"+traceback.format_exc()
    data['auth_status'] = s
    return render(request,"backend.html",data)
