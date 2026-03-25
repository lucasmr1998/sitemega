from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from builder.sitemaps import PageSitemap
from builder.views import page_view as homepage_view
from shortener.views import redirect_view as shortener_redirect

sitemaps = {'pages': PageSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),
    path('painel/', include('dashboard.urls')),
    path('api/', include('leads.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # Builder pages (/p/slug, /lojas)
    path('', include('builder.urls')),
    # Shortener catch-all BEFORE homepage (/<code> is more specific than '')
    path('<slug:code>', shortener_redirect, name='short_redirect'),
    # Homepage (empty path — last)
    path('', homepage_view, name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
