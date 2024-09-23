from datetime import datetime

from django.test import TestCase

from .models import Agenda

# Create your tests here.
class AgentaTest(TestCase):
    def setUp(self):
        Agenda.objects.create(nome='test',data_ini=datetime.now(),data_fim=datetime.now(),peso=1)
        Agenda.objects.create(nome='test2', data_ini=datetime.now(), data_fim=datetime.now(), peso=1)

    def test_agenda_criada(self):
        agenda1 = Agenda.objects.get(pk=1)
        agenda2 = Agenda.objects.get(pk=2)
        self.assertEqual(agenda1.nome,'test')
        self.assertEqual(agenda2.nome,'test2')
