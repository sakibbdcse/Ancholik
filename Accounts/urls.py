from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login, name='login'),
    path('register/',register, name='register'),
    path('logout/',logout, name='logout'),
    path('forgotten/',forgotten, name='forgotten'),
    path('success/',success, name='success'),
    path('verify/<auth_token>/',verify, name='verify'),
    path('fail/',fail, name='fail'),
]