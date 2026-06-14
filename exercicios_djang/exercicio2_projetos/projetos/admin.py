from django.contrib import admin
from .models import Pesquisador, TipoEntregavel, Projeto, Entregavel

admin.site.register(Pesquisador)
admin.site.register(TipoEntregavel)
admin.site.register(Projeto)
admin.site.register(Entregavel)
