from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
# Create your views here.

def main(request,category_slug=None):
    categories =None
    products=None
    
    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_active=True)
        product_count=products.count()
    else    :
        #categories=get_object_or_404(Category,category_slug=slug)
        products=Product.objects.filter(category=categories,is_active=True)
        product_count=products.count()
        
        
    products=Product.objects.all().filter(is_active=True)
    return render (request,'product/main.html',{'products':products}) 