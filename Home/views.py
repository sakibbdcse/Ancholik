from django.shortcuts import render
from Product.models import Category
from .models import HeroSlider  

# Create your views here.
def index(request):
    AllCategory = Category.objects.all()
    Heroslider = HeroSlider.objects.all()  
    return render(request, 'Home/home.html', locals())
