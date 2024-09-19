from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioDeRegistro, FormularioDeLogin


# Create your views here.

def home(request):
    return render(request,'registration/home.html')

def deslogar(request):
    logout(request)
    return redirect('/')

def logar(request):
    erro =  False
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