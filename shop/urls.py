from django.urls import path
from .views import shops

urlpatterns = [
    path('', shops, name='shop'),
]