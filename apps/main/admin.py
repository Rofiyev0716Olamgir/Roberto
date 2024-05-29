from atexit import register

from django.contrib import admin
from .models import Contact, Partner, Services


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('name', 'email', 'message')
    search_fields = ('name',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date',)
    list_display_links = ('name', 'create_date',)
    search_fields = ('name',)
    date_hierarchy = 'create_date'


@admin.register(Services)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date',)
    list_display_links = ('name', 'create_date',)
    search_fields = ('name',)
    date_hierarchy = 'create_date'