from django.contrib import admin
from .models import Supplier, PurchaseOrder, OrderItem

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields you want to display in the list view

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_supplier_name', 'order_date', 'status')  # Add other fields you want to display in the list view

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else 'No Supplier'
    get_supplier_name.short_description = 'Supplier'  # Displayed as column header in admin list view

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'purchase_order')  # Add other fields you want to display in the list view

