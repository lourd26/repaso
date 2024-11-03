from django.shortcuts import render,redirect
from home.models import Paleta
from home.forms import FormularioBusqueda,EdicionPaleta,EditarPerfil
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from home.models import Info

def home(request):
    return render (request,"home/index.html")

def paletas(request):
    
    formulario = FormularioBusqueda(request.GET)
    
    if formulario.is_valid():
        listado_paletas = Paleta.objects.filter(marca__icontains=formulario.cleaned_data.get('marca', ''))
        
    return render(request, 'home/paletas.html', {'form': formulario, 'paletas': listado_paletas})

class CrearPaleta(CreateView):
    model = Paleta
    template_name = "home/crear_paleta.html"
    fields = ['marca', 'anio', 'fecha_carga']
    success_url = reverse_lazy('home:paletas')
    
def eliminar_paleta(request, id_paleta):
    paleta = Paleta.objects.get(id=id_paleta)
    paleta.delete()
    return redirect('home:paletas')

def editar_paleta(request, id_paleta):
    
    paleta = Paleta.objects.get(id=id_paleta)
    
    formulario = EdicionPaleta(initial={'marca': paleta.marca,'anio': paleta.anio,'fecha_carga': paleta.fecha_carga})
    if request.method == "POST":
        formulario = EdicionPaleta(request.POST)
        if formulario.is_valid():
            
            paleta.marca = formulario.cleaned_data['marca']
            paleta.anio = formulario.cleaned_data['anio']
            paleta.fecha_carga = formulario.cleaned_data['fecha_carga']
            
            paleta.save()
            
            return redirect('home:paletas')
    
    return render(request, 'home/editar_paleta.html', {'form': formulario, 'paleta': paleta})

class VerPaleta(DetailView):
    model = Paleta
    template_name = "home/ver_paleta.html"

def login(request):
    
    formulario = AuthenticationForm()
    if request.method == "POST":
        
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            
            Info.objects.get_or_create(user=usuario)
            
            return redirect('home:editar_perfil')
    return render(request, 'home/login.html', {'form': formulario})

def editar_perfil(request):
    
    info = request.user.info
    
    formulario = EditarPerfil(instance=request.user, initial={'avatar': info.avatar})
    if request.method == "POST":
        
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            info.avatar = formulario.cleaned_data.get('avatar') if formulario.cleaned_data.get('avatar') else info.avatar
            info.save()
            
            formulario.save()
            
            return redirect('home:home')
    return render(request, 'home/editar_perfil.html', {'form': formulario})