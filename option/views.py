from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from news.models import News
from general.models import About
from django.http import HttpResponse
import re

def index(request):
    return render(request, 'index.html')

def home(request):
    news = News.objects.order_by('-created_at')[:4]
    about = About.objects.get(id=1)
    return render(request, 'home.html', {'news': news, 'about': about})

def locale(request):
    path = request.GET.get('path', '')
    locale = request.GET.get('locale', 'zh-tw')
    if path:
        if '/zh-cn' in path:
            match = re.match('/zh-cn(.+)', path)
            path = match.groups()[0]
        if '/zh-tw' in path:
            match = re.match('/zh-tw(.+)', path)
            path = match.groups()[0]
        if '/en' in path:
            match = re.match('/en(.+)', path)
            path = match.groups()[0]
        return redirect('/%s%s' % (locale, path))
    else:
        activate(locale)
        return redirect(reverse('home'))
