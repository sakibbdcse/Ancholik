from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Accounts/', include('Accounts.urls')),
    path('Cart/', include('Cart.urls')),
    path('Product/', include('Product.urls')),
    path('shop/', include('shop.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
