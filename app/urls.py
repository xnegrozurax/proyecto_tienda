from django.urls import path
from .views import *

urlpatterns = [
    path('' ,index , name="index"),
    path('login/',login, name="Login"),
    path('productos/',productos, name="productos"),
    path('registrarse/',registrarse, name="Registrarse"),
    path('carrito/',carrito, name="Carrito"),
    path('seguimiento/',seguimiento, name="Seguimiento"),
    path('usuariosub/',usuariosub, name="usuario-sub"),
    path('usuariodesub/',usuariodesub, name="usuario-desub"),
    path('agregar/',agregar, name="agregar"),
    path('modificar/<codigo>/',modificar, name="modificar"),
    path('listar/',listar, name="listar"),
    path('eliminar/<codigo>/',eliminar, name="eliminar"),
    path('agregarusuario/',agregarusuario, name="agregarusuario"),

]

