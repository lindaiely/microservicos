from django.db import models

class Adocao(models.Model):
    animal_nome = models.CharField(max_length=100)
    adotante_nome = models.CharField(max_length=100)
    data_adocao = models.DateField()
    status = models.CharField(max_length=1, choices=[('P', 'Pendente'), ('A', 'Aprovada'), ('R', 'Rejeitada')])

    def __str__(self):
        return f"{self.adotante_nome} adotou {self.animal_nome}"