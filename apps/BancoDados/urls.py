from django.urls import path
from .views import *

app_name = 'bancodados'

urlpatterns = [
    path('cadcategoria/', view_cadcategoria),
    path('create_categoria/', view_create_categoria, name='createcategoria'),
    path('cadcliente/', view_cadcliente),
    path('create_cliente/', view_create_cliente, name='createcliente'),
    path('caditenspedidos/', view_caditenspedidos, name='caditenspedidos'),
    path('create_itenspedidos/', view_create_itenspedidos, name='createitenspedidos'),
    path('cadmetpagamento/', view_cadmetpagamento),
    path('create_metpagamento/', view_create_metpagamento, name='createmetpagamento'),
    path('cadpedido/', view_cadpedido, name='cadpedido'),
    path('create_pedido/', view_create_pedido, name='createpedido'),
    path('cadproduto/', view_cadproduto, name="cadproduto"),
    path('create_produto/', view_create_produto, name='createproduto'),
]