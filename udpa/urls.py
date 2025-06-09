# udpa/urls.py
from django.urls import path
from . import views

app_name = 'udpa' # Namespace for your app's URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'), # Add this line
]