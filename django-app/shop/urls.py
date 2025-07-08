from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.products.urls')),
    path('chat/', include('shop.products.chat_urls')),
    path('', include('shop.products.urls')),
]
