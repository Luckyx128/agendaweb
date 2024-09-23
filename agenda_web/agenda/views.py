from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioDeRegistro, FormularioDeLogin
from .models import Agenda

# Create your views here.

def home(request):
    agendas:Agenda = Agenda.objects.all()
    return render(request,'registration/home.html',{'agendas':agendas})

def deslogar(request):
    logout(request)
    return redirect('/')

def logar(request):
    erro:bool =  False
    form = FormularioDeLogin()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            erro = True
    return render(request,'registration/login.html',{'form': form,'erro': erro})

@login_required
def painel(request):
    return render(request, 'painel.html')

def registrar(request):
    if request.method == 'POST':
        form = FormularioDeRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioDeRegistro()
    return render(request, 'registration/register.html', {'form': form})

def calcular(n1:int,n2:int)->int:
    result = n1+n2
    return result
