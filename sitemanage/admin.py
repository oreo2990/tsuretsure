from django.contrib import admin
from .models import SiteConfig
from django.contrib.sites.models import Site


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('id','meta_tittle',)
    list_display_links = ('meta_tittle',)

