from django.contrib import admin
from .models import Professor, Idioma, Curso, Estudante

admin.site.register(Professor)
admin.site.register(Idioma)
admin.site.register(Curso)
admin.site.register(Estudante)