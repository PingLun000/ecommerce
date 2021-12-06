from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name='product'

urlpatterns=[
    path('',views.productlists, name='productlists'),
    
]