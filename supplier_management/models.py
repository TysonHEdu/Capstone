from django.db import models

# Create your models here.
class Supplier_List(models.Model):
    name = models.CharField('Name', max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=100, default='CompanyA')


    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email} - {self.address} - {self.company}"