from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(blank=True, null=True)  # Optional field for contact details

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('lbs', 'Pounds'),
        ('oz', 'Ounces'),
        ('g', 'Grams'),
        # Add more units as needed
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='inventory_items', null=True)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    pack_size = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text='Specify pack size in the selected unit of measure')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, related_name='inventory_items', null=True, blank=True)

    def __str__(self):
        return self.name

    def total_cost(self):
        # Ensure that both cost_per_unit and pack_size have values before attempting to calculate
        if self.cost_per_unit and self.pack_size:
            return self.cost_per_unit * self.pack_size
        else:
            return 0  # Returns 0 if either cost_per_unit or pack_size is missing
