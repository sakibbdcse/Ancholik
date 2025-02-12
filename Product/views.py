from django.shortcuts import render
from .models import *
# Create your views here.
def product(request,id):
    product = Products.objects.filter(id=id)
    return render(request, 'Product/allProduct.html',locals())

def productDetails(request,id):
    productDetails = Products.objects.get(id=id)
    return render(request,'Product/singleProduct.html',locals())