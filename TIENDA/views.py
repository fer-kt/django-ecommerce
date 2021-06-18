import TIENDA
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Producto

# Create your views here.


def home(request):
    
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {
        'productos': productos
    })
    
    

def producto(request, id_producto):
    ctx = get_object_or_404(Producto, id = id_producto)
    return render(request, 'tienda/producto.html',{
        'ctx':ctx
        
    })