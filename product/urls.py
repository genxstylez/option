from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('product.views',
    url(r'^/$', 'index', name='product-index'),

)
