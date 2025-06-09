# udpa/admin.py
from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'property_type', 'price', 'bedrooms', 'bathrooms',
        'location', 'is_published', 'created_at'
    )
    list_filter = ('property_type', 'is_published', 'bedrooms', 'bathrooms', 'created_at')
    search_fields = ('title', 'description', 'location')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'property_type', 'price', 'is_published')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'built_up_area', 'land_area', 'amenities_proximity')
        }),
        ('Location', {
            'fields': ('location',)
        }),
        ('Images', {
            'fields': ('main_image', 'image_1', 'image_2', 'image_3'),
            'description': 'Upload up to 4 images for the property. Main image is required.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',), # Makes this section collapsible
        }),
    )