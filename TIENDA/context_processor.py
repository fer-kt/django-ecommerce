from .models import Categoria

def extras(request):
    categoria = Categoria.objects.all()
    return({ 'categoria': categoria})