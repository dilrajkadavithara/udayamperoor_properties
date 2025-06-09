from django.db import models

# Create your models here.
# udpa/models.py
from django.db import models
from django.utils import timezone # Import timezone for automatic timestamps

class Property(models.Model):
    # Choices for property_type
    PROPERTY_TYPE_CHOICES = [
        ('SALE', 'For Sale'),
        ('RENT', 'For Rent'),
    ]

    title = models.CharField(max_length=200, help_text="Title of the property (e.g., '3 BHK Villa in Riverside')")
    description = models.TextField(help_text="Detailed description of the property features and amenities.")
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES, default='SALE', help_text="Is the property for sale or rent?")

    price = models.DecimalField(max_digits=15, decimal_places=2, help_text="Price of the property (e.g., 5000000.00 for 50 Lakhs)")

    bedrooms = models.PositiveSmallIntegerField(default=1, help_text="Number of bedrooms.")
    bathrooms = models.PositiveSmallIntegerField(default=1, help_text="Number of bathrooms.")

    built_up_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Built-up area in Sq.Ft. (e.g., 1500.00)")
    land_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Land area in cents (e.g., 5.50 cents). Only if applicable for land/villa.")

    location = models.CharField(max_length=255, help_text="Exact address or landmark, e.g., 'Near St. Mary's Church, Udayamperoor'")
    amenities_proximity = models.TextField(blank=True, null=True, help_text="Comma-separated list of nearby amenities and their proximity (e.g., 'School: 1km, Hospital: 2km').")

    # Image fields - requires Pillow library (will install later if needed)
    # Images will be uploaded to MEDIA_ROOT/properties/ by default
    main_image = models.ImageField(upload_to='properties/', help_text="Main photo of the property.")
    image_1 = models.ImageField(upload_to='properties/', blank=True, null=True, help_text="Additional photo 1.")
    image_2 = models.ImageField(upload_to='properties/', blank=True, null=True, help_text="Additional photo 2.")
    image_3 = models.ImageField(upload_to='properties/', blank=True, null=True, help_text="Additional photo 3.")

    is_published = models.BooleanField(default=False, help_text="Check to make the property publicly visible.")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the property was added.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last update timestamp.")

    class Meta:
        verbose_name_plural = "Properties" # Plural name for admin
        ordering = ['-created_at'] # Order by most recently added by default

    def __str__(self):
        return self.title