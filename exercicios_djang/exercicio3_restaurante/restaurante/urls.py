from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.restaurantes_menu, name='restaurantes_menu'),
    path('reservas/', views.restaurantes_reservas, name='restaurantes_reservas'),
]