from django.contrib import admin

from .models import *
# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['article']


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'category__name']
    list_display = ['title', 'category', 'created_at', 'updated_at']
    list_filter = ['category', 'tags', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'content', 'article__title']
    list_display = ['article','name', 'email', 'content', 'created_at']
    list_filter = ['name', 'email', 'content', 'created_at']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)