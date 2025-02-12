from django.urls import path
from .views import *
urlpatterns = [
    path('product/<int:id>/', product, name='product'),
    path('product_details/<int:id>/', productDetails, name='productDetails'),
]