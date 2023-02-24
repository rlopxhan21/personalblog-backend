from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['slug', 'author', 'updated', 'active']
    list_filter= ['active', 'updated', 'author']
    search_fields = ['title', 'body', 'author']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    ordering = ['active', '-updated']

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['body', 'post', 'updated', 'active']
    list_filter= ['active', 'updated', 'post']
    search_fields = ['body', 'post']
    raw_id_fields = ['post']
    ordering = ['active', '-updated']
