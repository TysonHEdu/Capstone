from django import forms
from .models import PurchaseOrder, OrderItem

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier']  # Add other fields as needed
        

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity']  # Add other fields as needed