from django.urls import path
from . import  views

app_name='agenda'
urlpatterns = [
    path('',views.home,name='home'),
    path('painel/', views.painel, name='painel'),
    path('registrar/', views.registrar, name='registrar'),
    path('logar/',views.logar,name='logar'),
    path('deslogar/',views.deslogar,name='deslogar'),
]