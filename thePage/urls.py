from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^blog/', include('blog.urls')),
    url(r'^$', 'simple_cms.views.page', {'specific': 'home'}, name='home'),
    url(r'^(?P<specific>\w+)/$', 'simple_cms.views.page', name='page'),
)
