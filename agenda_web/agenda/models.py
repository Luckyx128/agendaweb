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