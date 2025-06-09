from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import personnelform
from .models import Task


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST   ['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(personnel)
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "Este usuario ya existe" 
                })
        return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': "Las contraseñas no coinciden" 
            })
    
#todo lo relacioando a los SUPER BOMBEROS DEL GER!! XDXDXDXD

#HECHO CON IA //////////////////// (hacia falta hacer que el personal se vea agrupado por turnos)
def personnel(request):
    JERARQUIA_ORDEN = {
        'CAPITAN': 0,
        'TENIENTE': 1,
        'SUBTENIENTE': 2,
        'BOMBERO_SUPERIOR': 3,
        'BOMBERO_CALIFICADO': 4,
    }
    tareas = Task.objects.select_related('turno').all()
    # Agrupar por turno
    grupos = {}
    for task in tareas:
        nombre_turno = task.turno.username
        if nombre_turno not in grupos:
            grupos[nombre_turno] = []
        grupos[nombre_turno].append(task)

    # Ordenar cada grupo por jerarquía
    for turno, personal in grupos.items():
        grupos[turno] = sorted(personal, key=lambda t: JERARQUIA_ORDEN.get(t.jerarquia, 99))

    return render(request, 'personnel.html', {'grupos': grupos})
# hasta aquii///////////////////////////////////////////////////////////////////


def add_personnel(request):
    if request.method == 'GET':
        return render(request, 'add_personnel.html',{
        'form': personnelform
        })
    else:
        try:
            form = personnelform(request.POST)
            new_personnal = form.save(commit=False)
            new_personnal.turno = request.user
            new_personnal.save()
            return redirect('personnel')
        except ValueError:
            return render(request, 'add_personnel.html', {
            'form': personnelform,
            'error': 'Por favor ingrese datos validos'
            })

def signout(request):
    logout(request)
    return redirect('home')

# Metodo para validar el logeo del usuario 
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect ('personnel')