from django.urls import path
from . import views

urlpatterns = [
    path('', views.escola_por_idioma, name='escola_por_idioma'),
    path('estudantes/', views.escola_por_estudante, name='escola_por_estudante'),
]