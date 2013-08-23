# coding: utf-8
from django.shortcuts import render
import re

def index(request):
    path = request.path
    product = 'images/brake-zh-tw.png'
    if '/zh-cn' in path:
        match = re.match('/zh-cn(.+)', path)
        path = match.groups()[0]
        product = 'images/brake-zh-cn.png'
    if '/en' in path:
        match = re.match('/en(.+)', path)
        path = match.groups()[0]
        product = 'images/brake-en.png'

    return render(request, 'product/index.html', {'product': product})
