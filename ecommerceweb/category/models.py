from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=255,unique=True)
    #url of category slug field cant accept any special charactor
    slug =models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    #where you upload to
    cart_image=models.ImageField(upload_to='photos/categories',blank=True)
    
    #data about data, used to correct the name given
    class Meta:
        verbose_name='category'
        #change the name in admin page because itj ust simply add s behind category
        verbose_name_plural='categories'
        
    def __str__(self):
        return self.category_name
    
