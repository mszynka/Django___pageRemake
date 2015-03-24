from django.contrib import admin
from simple_cms.models import *

# TODO tidy up

class ArticleInLine(admin.TabularInline):
    model = Article
    max_num = 0
    ordering = ('view',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'mail')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'logo')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','caption','image')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','view','date')
    # TODO exclude = (view.enabled = False)

class ViewAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','enabled')
    inlines = [ArticleInLine]
    ordering = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(View, ViewAdmin)