from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos_lista, name='projetos_lista'),
    path('pesquisadores/', views.pesquisadores_lista, name='pesquisadores_lista'),
]