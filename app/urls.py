
from django.contrib import admin
from django.urls import path
from weather.views import weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', weather, name="weather"),
]
