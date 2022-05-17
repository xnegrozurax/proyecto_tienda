from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

#SECCION AGREGAR

def agregar(request):
    datos= {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente!"

    return render(request, 'app/agregar.html', datos)

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/Login.html') 



#SECCION LISTAR     
def productos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaproductos' : productosAll
    }
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/productos.html' , datos)    

def registrarse(request):
    return render(request, 'app/Registrarse.html')
def seguimiento(request):
    return render(request, 'app/Seguimiento.html')



def carrito(request):
    carrito = Items_Carrito.objects.all()
    datos = { 'listaCarrito' : carrito }

    return render(request, 'app/Carrito.html', datos)


def usuariosub(request):
    return render(request, 'app/usuario-sub.html')
def usuariodesub(request):
    return render(request, 'app/usuario-desub.html')

def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaproductos' : productosAll
    }

    return render(request, 'app/listar.html' , datos) 
                                             
def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/modificar.html  ', datos)

def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar")    

def agregarusuario(request):
    datos= {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario agregado correctamente!"

    return render(request, 'app/agregarusuario.html', datos)  
