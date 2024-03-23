from django.urls import path
from . import views

urlpatterns = [
    path('supplier_management/', views.supplier_management, name='supplier_management'),
    path('supplierslist/', views.supplier_list, name='supplierslist'),
]