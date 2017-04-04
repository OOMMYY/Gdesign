#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render 

def hello(request):
    context          = {}
    context['hello'] = '这是变量表示的 Hello World!'
    return render(request, 'hello.html', context)
