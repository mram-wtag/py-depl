from django.urls import path
from .views import hello

urlpatterns = [
    # Other URL patterns...
    path('api/', hello),
]
