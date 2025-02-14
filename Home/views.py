from django.shortcuts import render
from Product.models import Category
from .models import HeroSlider  

# Create your views here.
def index(request):
    AllCategory = Category.objects.all()  
    HeroSliderList = HeroSlider.objects.all() 
    
    # Debugging: Print offer_name for each HeroSlider
    for hero in HeroSliderList:
        print(hero.offer_name)  # Access each hero's offer_name
    
    return render(request, 'Home/home.html', locals())
