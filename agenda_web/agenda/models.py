from contextlib import nullcontext
from datetime import datetime

from django.db import models
from django.db.models import DateTimeField, IntegerField, AutoField
from django.forms import CharField


# Create your models here.
class Agenda(models.Model):
    nome = models.CharField(max_length=200,default=f'agenda-{datetime.now()}')
    data_ini = models.DateTimeField()
    data_fim = models.DateTimeField()
    peso     = models.IntegerField()

    def __str__(self):
        return self.nome
class Status(models.Model):
    nome    = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome
    
class Card(models.Model):
    nome   = models.CharField(max_length=100)
    sprint = models.FloatField()
    peso   = models.CharField(max_length=2)
    id_agenda = models.ForeignKey(Agenda,on_delete=models.CASCADE)
    descricao = models.TextField()
    id_status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome

