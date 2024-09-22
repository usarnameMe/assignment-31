from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Car.urls')),
    path('api/', include('Animal.urls')),
]
