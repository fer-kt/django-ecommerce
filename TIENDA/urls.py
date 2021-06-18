from django.urls import path
from . import views


app_name = 'tienda'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('producto/<int:id_producto>', views.producto, name = 'producto')
    
]
