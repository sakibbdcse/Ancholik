from django.shortcuts import render
from Product.models import Products
def shops(request):
    product = Products.objects.all()
    return render(request, 'shop/allProduct.html',locals())