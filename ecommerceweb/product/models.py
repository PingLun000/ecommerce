from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    #used as a FK to retrieve data from Category Table
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)  
    #pre-defined by django in line 3, for User 
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_creator')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    description=models.TextField(blank=True)
    #image/ = path
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #-created's -means ordering by the last added items
        ordering=('-created',)
        
    def __str__(self):
        return self.title 