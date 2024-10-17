from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    
    def __str__(self):
        return self.nome
