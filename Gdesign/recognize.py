#!/usr/bin/env python
#coding:utf-8
from django import forms 
from django.shortcuts import render_to_response
from django.shortcuts import render
from veritification import  veritification
import shutil
import tensorflow as tf
import traceback
import os

class PictureForm(forms.Form):
    #图片
    imagefile=forms.ImageField()

def g0(request):
    return render_to_response('g0.html')

def recognize(request):
    print 'recognize'
    if request.method == 'POST':
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            image=request.FILES['imagefile']
            Pic=open("static/images/upload.jpg",'wb')
            for chunk in image.chunks():
                Pic.write(chunk)
            Pic.close()
    shutil.copyfile('static/images/upload.jpg','image/img_predict/predict.jpg')
    name = 'unknown'
    presion = 0.0
    try:
        with tf.Session():
            name, presion = veritification()
    except:
        print traceback.format_exc()
    os.remove('static/images/minPredict.jpg')
    shutil.copyfile('image/img_predict/minPredict.jpg','static/images/minPredict.jpg')
    data={}
    data['name'] = name
    data['presion'] = presion
    data['image']="static/images/upload.jpg"
    data['minPredict']='static/images/minPredict.jpg'
    return render(request,'g0.html',data)
