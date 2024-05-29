from django.contrib import admin
from .models import (
     BlogPost,
     Author,
     Content,
     Comments,
     Tag,
    BlogLike
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


class ContentAdminInline(admin.TabularInline):
    model = Content
    extra = 0


class CommentsInline(admin.TabularInline):
    fields = ('id', 'message')
    model = Comments
    extra = 0


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'create_date', )
    search_fields = ('name', 'tag', 'author')
    list_display_links = ('id', 'author', 'name', 'create_date', )
    readonly_fields = ('create_date', 'slug')
    date_hierarchy = 'create_date'
    filter_horizontal = ('tags',)
    inlines = [ContentAdminInline, CommentsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


@admin.register(BlogLike)
class EpisodeLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'author', )
    autocomplete_fields = ('author',)
    search_fields = ('blog', )
