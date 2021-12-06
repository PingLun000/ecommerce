from django.contrib import admin
from .models import Category
from django.db import models
# Register your models here.


 
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug']
    #prepopulated means the first field will follow whatever the second field insert
    prepopulated_fields={'slug':('category_name',)}
    
    
admin.site.register(Category, CategoryAdmin)