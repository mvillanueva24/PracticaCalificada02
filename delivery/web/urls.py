from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('detalle/<int:producto_id>/',views.detalle, name='detalle'),
    path('categoria/<int:category_id>/',views.categoria,name='categoria'),
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarProductoCarrito/<int:producto_id>',views.eliminarProductoCarrito,name="eliminarProductoCarrito"),
]