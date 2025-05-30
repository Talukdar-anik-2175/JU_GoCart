from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Search and Booking
    path('book-ride/', views.search_carts_page, name='book_ride'),

    # Driver Management
    path('driver/trips/', views.driver_trips, name='driver_trips'),

    # Services
    path('services/', views.services_view, name='services'),

    # price list
    path('pricing/', views.pricing_view, name='pricing'),

    # Contact Us
    path('contact/', views.contact_view, name='contact'),

]