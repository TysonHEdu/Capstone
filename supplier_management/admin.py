from django.contrib import admin

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

