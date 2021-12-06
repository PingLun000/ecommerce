from django.shortcuts import render
from .models import Product
# Create your views here.

def productlists(request):
    products=Product.objects.all().filter(is_active=True)
    return render (request,'product/home.html',{'products':products}) 