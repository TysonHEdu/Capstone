from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from inventory.models import Inventory

def aboutUs(request):
    # Your view logic here
    return HttpResponse("Hello, world!")

def homePage(request):
    servicesData = Service.objects.all()
    context = {
        'servicesData': servicesData,
    }
    return render(request, "index.html", context)

def saveEnquiry(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        produce = request.POST.get('produce')
        quantity = request.POST.get('quantity')
        # Assuming you have a model named Inventory to store the items
        # Create a new Inventory object and save it to the database
        item = Inventory(category=category, produce=produce, quantity=quantity)
        item.save()  # Save the item to the database
        # Redirect to the home page or any other appropriate page after adding the item
        return HttpResponse("Item added successfully!")
    else:
        return render(request, 'index.html')