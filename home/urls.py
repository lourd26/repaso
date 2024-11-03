from django.urls import path
from home import views

app_name="home"

urlpatterns = [
    path("",views.home,name="home"),
    path('paletas/', views.paletas, name='paletas'),
    path('paletas/crear/', views.CrearPaleta.as_view(), name='crear_paleta'),
    path('paletas/<int:pk>/', views.VerPaleta.as_view(), name='ver_paleta'),
    path('paletas/<int:id_paleta>/editar/', views.editar_paleta, name='editar_paleta'),
    path('paletas/<int:id_paleta>/eliminar/', views.eliminar_paleta, name='eliminar_paleta'),
    path('usuarios/login/', views.login, name='login'),
    path('usuarios/perfil/editar/', views.editar_perfil, name='editar_perfil'),

    
]

