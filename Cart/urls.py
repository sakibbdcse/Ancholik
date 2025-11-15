from django.urls import path
from .views import cart
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('/car', cart, name='cart'),
]