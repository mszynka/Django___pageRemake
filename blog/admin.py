from django.contrib import admin
from blog.models import Post, Category, Tag, BlogSettings

class BlogSettingsAdmin(admin.ModelAdmin):
	list_display = ('attribute','value')

class PostAdmin(admin.ModelAdmin):
	exclude = ['date']
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title','date','category','posted')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'slug')

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'slug')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(BlogSettings,BlogSettingsAdmin)