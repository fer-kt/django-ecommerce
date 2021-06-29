import django
from django.contrib.auth.models import Permission
from django.db.models.query_utils import Q
import TIENDA
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Categoria
from .forms import FormProducto, Producto
from django.urls import reverse
from django.contrib.auth.decorators import permission_required, login_required


def home(request):
    nuevos = Producto.objects.all().order_by('-fecha')[:3]
    productos = Producto.objects.all().order_by('-fecha')[3:10]
    categoria = Categoria.objects.all()
    return render(request, 'tienda/index.html', {
        'productos': productos,
        'nuevos': nuevos,
        'categoria': categoria,
    })


def producto(request, id_producto):
    categoria = Categoria.objects.all()
    ctx = get_object_or_404(Producto, id=id_producto)
    return render(request, 'tienda/producto.html', {
        'ctx': ctx,
        'categoria': categoria,

    })

@permission_required('TIENDA.add_producto')
def agregar(request):
    categoria = Categoria.objects.all()
    data = {"form": FormProducto(), 'categoria': categoria}
    if request.method == "POST":
        form = FormProducto(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda:home')
        else:
            form = FormProducto()
    return render(request, "tienda/agregar.html", data)


def categoria(request, id):
    categoria = Categoria.objects.all()
    cat = Producto.objects.filter(categoria=id)
    print(id)
    return render(request, 'tienda/categorias.html', {
        'cat': cat,
        'categoria': categoria
    })

@permission_required('TIENDA.producto_change')
def editar(request, id_producto):
    producto = get_object_or_404(Producto, id = id_producto)
    if request.method == 'POST':
        form = FormProducto(data=request.POST, files=request.FILES, instance= producto)
        if form.is_valid():
            form.save()
            return redirect('tienda:home')
    else:
        form = FormProducto(instance= producto)
        return render(request, 'tienda/editar.html', {
            'producto': producto,
            'form': form
        })
@permission_required('TIENDA.delete_producto')
def eliminar(request, articulo_id):
    producto = get_object_or_404(Producto, id=articulo_id)
    producto.delete()
    return redirect("tienda:home")


def buscar(request):
    buscar = request.GET['buscar']
    producto = Producto.objects.filter(
        Q(descripcion__contains = buscar) | Q(titulo__contains=buscar) )
    
    return render(request, 'tienda/buscar.html', {
        'categoria':Categoria.objects.all(),
        'producto': producto,
        
    })