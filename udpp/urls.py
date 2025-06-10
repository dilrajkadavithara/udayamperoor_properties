# udpp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static
from django.contrib.sitemaps.views import sitemap
from udpa.sitemaps import StaticViewSitemap, PropertySitemap # Import your sitemap classes

sitemaps = {
    'static': StaticViewSitemap,
    'properties': PropertySitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('udpa.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# Add this block for serving media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)