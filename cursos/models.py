from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    data_de_criação = models.DateField()
    ativo = models.BooleanField(default= True)
    
    def __str__(self):
        return self.nome
    