from django.db import models

# Create your models here.
class SuppliersList(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.field1  # Return a string representation of the model instance