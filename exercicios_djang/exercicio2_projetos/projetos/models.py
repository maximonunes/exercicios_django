from django.db import models

class Pesquisador(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class TipoEntregavel(models.Model):
    nome = models.CharField(max_length=100)  # artigo, relatório, software
    def __str__(self): return self.nome

class Projeto(models.Model):
    titulo       = models.CharField(max_length=200)
    resumo       = models.TextField()
    data_inicio  = models.DateField()
    coordenador  = models.ForeignKey(
        Pesquisador, on_delete=models.CASCADE,
        related_name='projetos_coordenados'
    )
    pesquisadores = models.ManyToManyField(
        Pesquisador, related_name='projetos_associados', blank=True
    )
    def __str__(self): return self.titulo

class Entregavel(models.Model):
    projeto      = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='entregaveis')
    tipo         = models.ForeignKey(TipoEntregavel, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    link         = models.URLField()
    def __str__(self): return f'{self.tipo} - {self.projeto}'