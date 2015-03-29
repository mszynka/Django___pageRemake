from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^$', 'simple_cms.views.home', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),
		url(r'^blog/', include('blog.urls')),
=======
    url(r'^$', 'simple_cms.views.page', {'specific': 'home'}, name='home'),
    url(r'^(?P<specific>\w+)/$', 'simple_cms.views.page', name='page'),
    (r'^ckeditor/', include('ckeditor.urls')),
>>>>>>> merge
    url(r'^admin/', include(admin.site.urls)),
)
