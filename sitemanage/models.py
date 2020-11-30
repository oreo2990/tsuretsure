from django.db import models
from django.contrib.sites.models import Site


class SiteConfig(models.Model):
    site = models.OneToOneField(Site, verbose_name='Site', on_delete=models.PROTECT)
    meta_tittle = models.CharField('meta_tittle',max_length=100)
    meta_description = models.CharField('meta_description',max_length=300)
    meta_keywords = models.CharField('SEOキーワード',max_length=300)
    author = models.CharField('管理者',max_length=30)
    top_tittle = models.CharField('TOPページタイトル',max_length=100)
    top_subtittle = models.CharField('TOPページサブタイトル',max_length=200)

    def __str__(self):
        return self.meta_tittle