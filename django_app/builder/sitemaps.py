from django.contrib.sitemaps import Sitemap
from .models import Page


class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Page.objects.filter(status='published', noindex=False)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
