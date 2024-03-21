from django.urls import path
from . import views

urlpatterns = [
    path('supplier_management/', views.supplierslist, name='suppliers_list'),
]