from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity', 'unit_price']

# Register your models here
admin.site.register(Service, ServiceAdmin)
