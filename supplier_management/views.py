from django.shortcuts import render
from .models import SuppliersList

def suppliers_list(request):
    return render(request, 'supplier_management/suppliermanagement.html')