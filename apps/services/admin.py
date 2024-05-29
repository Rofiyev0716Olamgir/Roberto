from django.contrib import admin
from .models import (
     ServicesPost,
     Content,
     Category,
     Tag,
    ServiceLike
)


class ContentAdminInline(admin.TabularInline):
    model = Content
    extra = 0


@admin.register(ServicesPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date', )
    search_fields = ('name', 'tag')
    list_display_links = ('id', 'name', 'create_date', )
    readonly_fields = ('create_date', 'slug')
    date_hierarchy = 'create_date'
    filter_horizontal = ('tags',)
    inlines = [ContentAdminInline,]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')

@admin.register(ServiceLike)
class EpisodeLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'author', )
    autocomplete_fields = ('author',)
    search_fields = ('blog', )