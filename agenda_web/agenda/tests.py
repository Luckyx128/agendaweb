from datetime import datetime

from django.test import TestCase

from agenda_web.agenda.models import Agenda

# Create your tests here.
class AgentaTest(TestCase):
    def setUp(self):
        Agenda.objects.create(name='test',data_ini=datetime.now(),data_fim=datetime.now()+5,peso=1)
        Agenda.objects.create(name='test2', data_ini=datetime.now(), data_fim=datetime.now() + 5, peso=1)

    def test_agenda_criada(self):
        agenda = Agenda.objects.get('test')
        self.assertEqual(agenda.nome,'test')