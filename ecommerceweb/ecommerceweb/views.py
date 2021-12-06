from django.shortcuts import render
from product.models import Product
def home(request):
    
    #assign a new variable to store the result
    products=Product.objects.all().filter(is_active=True)
    
    #context={
    #    'products':products,
    # }
    return render(request,'./home.html',{'products':products})