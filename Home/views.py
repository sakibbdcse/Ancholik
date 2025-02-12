from django.shortcuts import render
from Product.models import Category
# Create your views here.
def index(request):
    AllCategory = Category.objects.all()
    return render(request, 'Home/home.html', locals())