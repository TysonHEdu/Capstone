from django.views.generic import ListView
from django.shortcuts import render
from .models import InventoryItem
from .models import Category

class HomePageView(ListView):
    model = InventoryItem
    template_name = 'home.html'
    context_object_name = 'inventory_items'

def categories_list(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    selected_category = None

    if selected_category_id:
        category = Category.objects.get(pk=selected_category_id)
        inventory_items = category.inventory_items.all()
        selected_category = category.name
    else:
        inventory_items = []

    return render(request, 'inventory/categories.html', {'categories': categories, 'inventory_items': inventory_items, 'selected_category': selected_category})