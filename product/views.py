# coding: utf-8

def index(request):
    path = request.path
    template = 'product/index.html'
    if '/zh-cn' in path:
        match = re.match('/zh-cn(.+)', path)
        path = match.groups()[0]
        template = 'product/index-cn.html'
    if '/en' in path:
        match = re.match('/zh-cn(.+)', path)
        path = match.groups()[0]
        template = 'product/index-en.html'

    return render(request, template)
