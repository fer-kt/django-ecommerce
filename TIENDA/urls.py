from django.urls import path
from . import views


app_name = 'tienda'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('producto/<int:id_producto>', views.producto, name = 'producto'),
    path('agregar/', views.agregar, name = 'agregar'),
    path('categoria/<int:id>', views.categoria, name = 'categorias'),
    path('editar/<int:id_producto>', views.editar, name = 'editar'),
    path('eliminar/<articulo_id>', views.eliminar, name = 'eliminar'),
    path('buscar/', views.buscar, name = 'buscar')
]
