from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()
    context = {
        'product_list' : product_list,
        'category_list' : category_list
        }
    return render(request, 'index.html', context)
    
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    category_list = Categoria.objects.all()
    return render(request, 'detalle.html', {'producto' : producto, 'category_list' : category_list})

def categoria(request, category_id):
    category_list = Categoria.objects.all()
    product_list = Producto.objects.filter(categoria_id = category_id)
    return render(request,'categorias.html',{'product_list' : product_list,'category_list' : category_list})

from web.carrito import Cart

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')