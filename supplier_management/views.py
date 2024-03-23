from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Supplier_List

def supplier_management(request):
    template = loader.get_template('suppliermanagement.html')
    return HttpResponse(template.render())


def supplier_list(request):
    supplier_list = Supplier_List.objects.all()
    return render(request, 'suppliermanagement.html', 
            {'supplier_list': supplier_list})