from django.contrib import admin
from core.models import Page


class RCoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page')
    list_filter = ('id', 'page',)
    search_fields = ('body', 'title',)
    ordering = ('id',)

admin.site.register(Page, RCoreAdmin)