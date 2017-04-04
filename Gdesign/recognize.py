#coding:utf-8
from django import forms 

class PictureForm(forms.Form):
	#图片
	imagefile=forms.ImageField()

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf

def g0(request):
    return render_to_response('g0.html')

def recognize(request):
	if request.method == 'POST':
		form = PictureForm(request.POST,request.FILES)
		if form.is_valid():
			image=request.FILES['imagefile']
			Pic=open("static/images/upload.jpg",'ab')
			for chunk in image.chunks():
				Pic.write(chunk)
			Pic.close()
	data={}
	data['image']="/static/images/a.jpg"
	return render(request,'g0.html',data)
