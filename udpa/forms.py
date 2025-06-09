# udpa/forms.py
from django import forms
from .models import Property

class PropertyFilterForm(forms.Form):
    # Choices are derived from the Property model's PROPERTY_TYPE_CHOICES
    PROPERTY_TYPE_CHOICES = [('', 'Any Type')] + list(Property.PROPERTY_TYPE_CHOICES)

    keyword = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Search by Location or Keyword', 'class': 'form-input w-full'}),
        label="" # Hide default label, using placeholder
    )
    property_type = forms.ChoiceField(
        choices=PROPERTY_TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select w-full'})
    )
    min_price = forms.DecimalField(
        required=False,
        max_digits=15,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Min Price', 'class': 'form-input w-full'})
    )
    max_price = forms.DecimalField(
        required=False,
        max_digits=15,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Max Price', 'class': 'form-input w-full'})
    )
    bedrooms = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Beds', 'class': 'form-input w-full'})
    )
    bathrooms = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Baths', 'class': 'form-input w-full'})
    )