# udpa/views.py
from django.shortcuts import render,get_object_or_404
from .models import Property
from .forms import PropertyFilterForm
from django.db import models
from django.core.paginator import Paginator # Import Paginator

def home(request):
    return render(request, 'udpa/home.html')

def property_list(request):
    form = PropertyFilterForm(request.GET)
    properties = Property.objects.filter(is_published=True)

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        property_type = form.cleaned_data.get('property_type')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        bedrooms = form.cleaned_data.get('bedrooms')
        bathrooms = form.cleaned_data.get('bathrooms')

        if keyword:
            properties = properties.filter(
                models.Q(title__icontains=keyword) |
                models.Q(description__icontains=keyword) |
                models.Q(location__icontains=keyword)
            )
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)
        if bedrooms:
            properties = properties.filter(bedrooms__gte=bedrooms)
        if bathrooms:
            properties = properties.filter(bathrooms__gte=bathrooms)

    # Order the filtered properties
    properties = properties.order_by('-created_at')

    # --- PAGINATION ---
    # Show 6 properties per page
    paginator = Paginator(properties, 6) # Create a Paginator object
    page_number = request.GET.get('page') # Get the current page number from the URL
    page_obj = paginator.get_page(page_number) # Get the Page object for the requested page
    # --- END PAGINATION ---

    context = {
        'properties': page_obj, # Pass the Page object instead of the full queryset
        'form': form,
    }

    return render(request, 'udpa/property_list.html', context)

def property_detail(request, pk): # pk stands for primary key
    # Fetch a single property by its primary key (ID)
    # get_object_or_404 will raise a 404 error if the property doesn't exist
    property_obj = get_object_or_404(Property, pk=pk, is_published=True)

    context = {
        'property': property_obj # Pass the single property object to the template
    }

    return render(request, 'udpa/property_detail.html', context)