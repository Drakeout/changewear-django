from django.contrib.auth.models import Group
from django.core.checks import messages
from django.core.files.images import ImageFile
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from core.models import *
from core.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import json
from core.decorators import *
import random
# Create your views here.

def home_page(request):
    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None
    
    
    return render(request, 'pages/home.html', context)

    
def mujer_page(request):

    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    context['nombre'] = 'Mujer'

    return render(request, 'pages/categoria.html', context)

def hombre_page(request):
    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    context['nombre'] = 'Hombre'

    return render(request, 'pages/categoria.html', context)

def nino_page(request):
    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    context['nombre'] = 'Niños'

    return render(request, 'pages/categoria.html', context)

def producto_page(request, pk):
    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    producto = Producto.objects.get(id=pk)
    context['producto'] = producto
    return render(request, 'pages/producto.html', context)

# Clientes
def registrarse_page(request):
    form1 = CreateUserForm()
    form2 = ClienteForm()

    if request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = ClienteForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            apellido_paterno = request.POST.get('apellido_paterno')
            apellido_materno = request.POST.get('apellido_materno')
            telefono = request.POST.get('telefono')

            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            Cliente.objects.create(
                usuario = user,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                telefono=telefono
            )

            messages.success(request, 'Cuenta creada con exito')
            return redirect('login_page')
        else:
            messages.error(request, 'La cuenta no pudo ser creada')

    context = {'formUser': form1, 'formCliente': form2}
    return render(request, 'pages/register.html', context)

@usuario_identificado
def login_page(request):
    context = {}

    if request.method == 'POST':
        correo = request.POST.get('email')
        password = request.POST.get('password')

        usuario = User.objects.get(email=correo)
        print(usuario.username)

        user = authenticate(request, username=usuario.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')


    return render(request, 'pages/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page') 



#TO-DO: Agregar condición para logeado y para clientes con decoradores
@login_required(login_url='home_page')
def carro_page(request):
    cliente = request.user.cliente
    compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
    items = compra.productocompra_set.all()
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
    except:
        carro = None
    
    context = {'items': items, 'compra': compra, 'carro':carro}
    return render(request, 'pages/carro.html', context)


def direccion_page(request, pk):
    form = DireeccionForm()
    compra = Compra.objects.get(id=pk)
    cliente = request.user.cliente

    if request.method == 'POST':
        form = DireeccionForm(request.POST)
        if form.is_valid():
            form.instance.cliente = cliente
            form.instance.compra = compra
            form.save()

            messages.success(request, 'Direccion agregada')

            return redirect('pagar_page')
        else:
            messages.error(request, 'No se pudo agregar la dirección')

    context = {'form': form}
    return render(request, 'pages/direccion.html', context)

@login_required(login_url='home_page')
def pagar_page(request):
    #TO-DO: Agregar try and catch para cada variable, excepto cliente
    cliente = request.user.cliente
    compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
    items = compra.productocompra_set.all()

    if request.method == 'POST':
        compra_comp = Compra.objects.filter(id=compra.id).update(completado=True)
        messages.success(request, 'Producto comprado')

   
    
    context = {'items': items, 'compra': compra}
    return render(request, 'pages/pagar.html', context)

def vision_page(request):
    context = {}

    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    return render(request, 'pages/vision.html', context)


#TO-DO: datos de formularios para Empleo y Contacto

def contacto_page(request):
    context = {}

    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    return render(request, 'pages/contacto.html', context)

def cambios_page(request):
    context = {}

    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    return render(request, 'pages/cambios.html', context)

def empleo_page(request):
    context = {}

    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None

    return render(request, 'pages/empleo.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productoId = data['productId']
    action = data['action']

    cliente = request.user.cliente
    producto = Producto.objects.get(id=productoId)
    compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)

    productoCompra, creada = ProductoCompra.objects.get_or_create(compra=compra, producto=producto)

    if action == 'add':
        productoCompra.cantidad = (productoCompra.cantidad + 1)
    elif action == 'remove':
        productoCompra.cantidad = (productoCompra.cantidad - 1)

    productoCompra.save()

    if productoCompra.cantidad <= 0:
        productoCompra.delete() 

    return JsonResponse('Item fue añadido', safe=False)


def user_page(request, action):
    context = {}
    cliente = request.user.cliente
    context['cliente'] = cliente
    compras = Compra.objects.all().filter(cliente=cliente, completado=True)
    context['compras'] = compras
    envios = DireccionEnvio.objects.all().filter(cliente=cliente)
    context['envios'] = envios
    
    # mecanica carro
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None
    
    try: 
        compras_completas = DireccionEnvio.objects.all().filter(cliente=cliente,entregado=True)
        context['compras_completas'] = compras_completas
    except:
        context['compras_completas'] = None


    return render(request, 'pages/user.html', context)

def admin_page(request, action):
    context = {}
    try:
        envios = DireccionEnvio.objects.all().filter(entregado=False)
        context['envios'] = envios
    except:
        context['envios'] = None
    try:
        compras = Compra.objects.all().filter(completado=True)
        context['compras'] = compras
    except:
        context['compras'] = None
    try:
        productos = Producto.objects.all()
        context['productos'] = productos
    except:
        context['productos'] = None

    
    if action == 'inicio':
        context['nombre'] = 'Inicio'
    elif action == 'productos':
        context['nombre'] = 'Productos'
    elif action == 'envios':
        context['nombre'] = 'Envíos'
    elif action == 'compras':
        context['nombre'] = 'Compras'

    return render(request, 'pages/funcionarios.html', context)

    
def preguntas_frecuentes(request):
    context = {}
    try:
        cliente = request.user.cliente
        compra, creada = Compra.objects.get_or_create(cliente=cliente, completado=False)
        items = compra.productocompra_set.all()
        
        carro = compra.get_comprar_productos
        context['carro'] = carro
        context['items'] = items
    except:
        carro = None
        items = None
    
    
    return render(request, 'pages/preguntas_frecuentes.html', context)
def crud_producto(request, pk):
    context = {}
    form = ProductoForm()
    try:
        producto = Producto.objects.get(id=pk)
        form = ProductoForm(instance=producto)
        context['form'] = form
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto agregado')
            else:
                messages.error(request, 'Error al guardar el producto')
        
    except:
        context['form'] = form
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto agregado')
            else:
                messages.error(request, 'Error al guardar el producto')


    
    return render(request, 'pages/func-produc.html', context)



def poblar_bd(request):
    
    #Borra los productos existentes 
    Producto.objects.all().delete()

    #Agrega productos a la base de datos
    Producto.objects.create(titulo="Camisa Hombre Negra Dorada", precio='21000', categoria="HM", descripcion="Camisa de vestir de colores negro y dorado. Diseño oriental.", imagen="h-camisa.jpg")
    Producto.objects.create(titulo="Pantalones Cuero Hombre Negros", precio='32000', categoria="HM", descripcion="Pantalones de cuero color negro. Cinturon no incluido.", imagen="h-pantalones.jpg")
    Producto.objects.create(titulo="Zapatos Cuero Cafe", precio='45000', categoria="HM", descripcion="Zapatos de cuero color marron. Hebilla de plata. Disponible en todas tallas.", imagen="h-zapato.jpg")
    Producto.objects.create(titulo="Blusa Multicolor Sparkle", precio='42000', categoria="MJ", descripcion="Top tipo blusa multicolor, refleja la luz. Spaghetti strap.", imagen="m-blusa.jpg")
    Producto.objects.create(titulo="Vestido Mujer de Una Pieza", precio='15000', categoria="MJ", descripcion="Vestido negro y azul. Una pieza, disponible en todas las tallas.", imagen="m-vestido.jpg")
    Producto.objects.create(titulo="Flats Negros Mujer", precio='66000', categoria="MJ", descripcion="Zapatos Flat de mujer, disponibles en Negro y Blanco. Taco bajo.", imagen="m-zapato.jpg")
    Producto.objects.create(titulo="Buso Oso de Niño", precio='12500', categoria="NN", descripcion="Buso de niño unisex. Diseño de oso, disponible en verde, rojo y azul.", imagen="n-buso.jpg")
    Producto.objects.create(titulo="Pantalones Dinosario de Niño", precio='14000', categoria="NN", descripcion="Pantalones de buso unisex para niños, diseño de dinosaurio, disponible en gris y negro.", imagen="n-pantalones.jpg")
    Producto.objects.create(titulo="Zapatillas con Luces de Niño", precio='27000', categoria="NN", descripcion="Zapatillas unisex para niños, con luces fluorecentes en la suela. Baterias incluidas.", imagen="n-zapatilla.jpg")
    
    #Redirige a la pagina catalogo de hombres
    return redirect('home_page')
