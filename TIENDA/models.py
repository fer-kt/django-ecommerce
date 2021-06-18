from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length= 100, null=False)
    descripcion = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f'{self.titulo} '


class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes')
    descripcion = models.TextField(max_length=1000)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='categoria_producto')

    def __str__(self) -> str:
        return f'{self.titulo} - {self.categoria} '

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    lista = models.ManyToManyField(Producto)
    #total 
    
    def __str__(self) -> str:
        return f'{self.usuario}, {self.lista} '
    