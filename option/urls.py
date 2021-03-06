from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.i18n import set_language

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'option.views.home', name='home'),
    url(r'^$', 'option.views.index', name='index'),
    url(r'^locale/$', 'option.views.locale', name='locale'),
    
    (r'^grappelli/', include('grappelli.urls')),
    # url(r'^option/', include('ylauto.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 
urlpatterns += i18n_patterns('',
    url(r'^home/$', 'option.views.home', name='home'),
    url(r'^about/', 'general.views.about', name='about'),
    url(r'^contact/', 'general.views.contact', name='contact'),
    url(r'^news/', include('news.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^product/', include('product.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
