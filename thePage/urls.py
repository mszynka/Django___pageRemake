from django.conf.urls import patterns, include, url
from django.contrib import admin
from simple_cms.views import home

urlpatterns = patterns('',
    url(r'^$', 'simple_cms.views.home', name='home'),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
