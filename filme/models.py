from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    avaliacao = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.titulo
