from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Property  # Assuming your Property model is in udpa/models.py

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        # List of names of static views to include in the sitemap
        # Make sure these view names correspond to your Django URL names in udpa/urls.py
        return ['udpa:home', 'udpa:property_list'] # Assuming you have URL names 'home' and 'property_list'

    def location(self, item):
        return reverse(item)

class PropertySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        # Fetch all published/active properties if applicable, e.g., Property.objects.filter(is_published=True)
        return Property.objects.all()

    def lastmod(self, obj):
        # IMPORTANT: Replace 'updated_at' with the actual field name from your Property model
        # that indicates the last time the object was modified (e.g., 'created_at', 'timestamp').
        # If you don't have such a field, you can return None, or remove this method.
        return obj.updated_at 

    def location(self, obj):
        # IMPORTANT: Replace 'udpa:property_detail' with the actual URL name for your property detail page.
        # Replace 'slug' with your actual lookup field (e.g., 'pk' for primary key/ID, or 'id', or 'your_slug_field').
        return reverse('udpa:property_detail', args=[obj.slug])