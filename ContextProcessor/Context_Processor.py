from Product.models import Category

def category_list(request):
    AllCategory = Category.objects.all()
    return{'AllCategory': AllCategory}