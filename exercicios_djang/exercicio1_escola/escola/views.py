from django.shortcuts import render
from .models import Idioma, Estudante


def escola_por_estudante(request):
    estudantes = Estudante.objects.prefetch_related('cursos__idioma')
    return render(request, 'escola/por_estudante.html', {'estudantes': estudantes})

def escola_por_idioma(request):
    idiomas = Idioma.objects.prefetch_related('cursos__professor', 'cursos__estudantes')
    return render(request, 'escola/por_idioma.html', {'idiomas': idiomas})