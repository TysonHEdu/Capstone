from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Purchase
from django.contrib import messages
from inventory.models import InventoryItem

def calculate_order_total(order_id):
    order = Order.objects.get(id=order_id)
    total = sum(item.quantity * item.unit_price for item in order.items.all())
    return total

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    total = calculate_order_total(order_id)
    return render(request, 'orders/order_detail.html', {'order': order, 'total': total})

def create_purchase(request):
    if request.method == 'POST':
        # Process form data
        # Assuming form includes fields like item_id and quantity
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        
        # Reduce inventory level
        item = InventoryItem.objects.get(id=item_id)
        if item.quantity >= int(quantity):
            item.quantity -= int(quantity)
            item.save()
            # Create purchase record
            Purchase.objects.create(item=item, quantity=quantity)
            messages.success(request, 'Purchase created successfully.')
            return redirect('purchase_list')
        else:
            messages.error(request, 'Insufficient inventory.')
            return redirect('create_purchase')
    else:
        # Render purchase form
        return render(request, 'purchases/create_purchase.html')