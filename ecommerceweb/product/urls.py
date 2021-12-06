from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name='product'

urlpatterns=[
    path('',views.main, name='main'),
    path('<slug:category_slug>/',views.main, name='products_by_category'),
    
]