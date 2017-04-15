#!/usr/bin/env
#coding:utf-8
"""Gdesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url
from django.contrib import admin
from . import recognize,backend,view
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^g0$',recognize.g0),
    url(r'^recognize$',recognize.recognize),
    url(r'^backend$',backend.menu),
    url(r'^backend_preview',backend.preview),
    url(r'^backend_auth',backend.auth),
    url(r'^$',view.hello)
]


