from django.shortcuts import render
from .models import InventoryItem

def home(request):
    # Logic to retrieve inventory items
    inventory_items = InventoryItem.objects.all()
    return render(request, 'home.html', {'inventory_items': inventory_items})

def categories(request):
    # Logic to retrieve categories and associated inventory items
    categories = ['Vegetables', 'Meat', 'Frozen Items', 'Beverages']  # Example list of categories
    inventory_items = {}  # Example dictionary mapping categories to inventory items
    return render(request, 'categories.html', {'categories': categories, 'inventory_items': inventory_items})
