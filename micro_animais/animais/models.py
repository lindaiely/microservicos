from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=1, choices=[('C', 'Cachorro'), ('G', 'Gato'), ('O', 'Outro')])
    idade = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome