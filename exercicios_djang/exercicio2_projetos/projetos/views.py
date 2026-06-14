from django.shortcuts import render
from .models import Projeto, Pesquisador

def projetos_lista(request):
    projetos = Projeto.objects.select_related('coordenador').prefetch_related(
        'pesquisadores', 'entregaveis__tipo'
    )
    return render(request, 'projetos/lista.html', {'projetos': projetos})


def pesquisadores_lista(request):
    pesquisadores = Pesquisador.objects.prefetch_related(
        'projetos_coordenados', 'projetos_associados'
    )
    return render(request, 'projetos/pesquisadores.html', {'pesquisadores': pesquisadores})