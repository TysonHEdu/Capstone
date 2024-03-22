from django.shortcuts import render, redirect, get_object_or_404
from .forms import PurchaseOrderForm, OrderItemForm
from .models import PurchaseOrder

def create_purchase_order(request):
    if request.method == 'POST':
        purchase_order_form = PurchaseOrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)
        if purchase_order_form.is_valid() and order_item_form.is_valid():
            purchase_order = purchase_order_form.save()
            order_item = order_item_form.save(commit=False)
            order_item.purchase_order = purchase_order
            order_item.save()
            return redirect('purchase_order_detail', pk=purchase_order.pk)
    else:
        purchase_order_form = PurchaseOrderForm()
        order_item_form = OrderItemForm()
    return render(request, 'create_purchase_order.html', {'purchase_order_form': purchase_order_form, 'order_item_form': order_item_form})

def purchase_order_detail(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    return render(request, 'purchase_order_detail.html', {'purchase_order': purchase_order})