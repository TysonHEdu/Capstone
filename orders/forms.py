from django import forms
from .models import PurchaseOrder, OrderItem

class PurchaseOrderForm(forms.ModelForm):
    supplier_name = forms.CharField(max_length=100, label='Supplier Name')  # Add this line
    class Meta:
        model = PurchaseOrder
        fields = ['status']  # Add other fields as needed
        

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity']  # Add other fields as needed