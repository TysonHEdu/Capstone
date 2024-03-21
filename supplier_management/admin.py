from django.contrib import admin

# Register your models here.
class SuppliersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(SuppliersList, SuppliersListAdmin)