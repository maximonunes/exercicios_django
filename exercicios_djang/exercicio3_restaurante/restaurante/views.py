from django.shortcuts import render
from .models import Restaurante, Categoria

def restaurantes_menu(request):
    restaurantes = Restaurante.objects.prefetch_related('pratos__categoria')
    categorias   = Categoria.objects.all()
    return render(request, 'restaurante/menu.html', {
        'restaurantes': restaurantes,
        'categorias': categorias
    })


def restaurantes_reservas(request):
    restaurantes = Restaurante.objects.prefetch_related(
        'reservas__cliente'
    ).all()
    return render(request, 'restaurante/reservas.html', {'restaurantes': restaurantes})