from django.db import models
from django.contrib.auth.models import User


class Paleta(models.Model):
    marca = models.CharField(max_length=20)
    anio = models.IntegerField()
    fecha_carga = models.DateField()
    
    def __str__(self):
        return f"{self.marca} {self.anio}"

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=False)