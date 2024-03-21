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