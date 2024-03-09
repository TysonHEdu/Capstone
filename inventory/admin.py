from django.contrib import admin
from .models import InventoryItem, Category, Supplier

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'cost_per_unit', 'pack_size', 'display_total_cost')
    
    def display_total_cost(self, obj):
        return obj.total_cost()
    display_total_cost.short_description = 'Total Cost ($)'

admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(Category)
admin.site.register(Supplier)