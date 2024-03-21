from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('orders/', include('orders.urls')),
    # Add other URL patterns as needed
]