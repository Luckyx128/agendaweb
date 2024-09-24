from django.contrib import admin

from .models import Agenda,Card,Status
# Register your models here.

admin.site.register(Agenda)
admin.site.register(Card)
admin.site.register(Status)