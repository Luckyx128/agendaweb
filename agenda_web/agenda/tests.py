from datetime import datetime

from django.test import TestCase

from .models import Agenda

# Create your tests here.
class AgentaTest(TestCase):
    def setUp(self):
        Agenda.objects.create(nome='test',data_ini=datetime.now(),data_fim=datetime.now(),peso=1)
        Agenda.objects.create(nome='test2', data_ini=datetime.now(), data_fim=datetime.now(), peso=1)

    def test_agenda_criada(self):
        agenda = Agenda.objects.get(pk=2)
        self.assertEqual(agenda.nome,'test')