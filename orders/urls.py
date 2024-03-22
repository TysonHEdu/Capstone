from django.urls import path
from .views import create_purchase_order, purchase_order_detail

urlpatterns = [
    path('create_purchase_order/', create_purchase_order, name='create_purchase_order'),
    # Other URL patterns if any
    
     path('purchase_order_detail/<int:pk>/', purchase_order_detail, name='purchase_order_detail'),
]
