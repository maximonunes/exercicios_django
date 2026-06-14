from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Idioma(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Curso(models.Model):
    nome      = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    idioma    = models.ForeignKey(Idioma,    on_delete=models.CASCADE, related_name='cursos')
    def __str__(self): return self.nome

class Estudante(models.Model):
    nome   = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, related_name='estudantes')
    def __str__(self): return self.nome