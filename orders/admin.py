from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_amount', 'is_completed')
    list_filter = ('user', 'created_at', 'is_completed')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)