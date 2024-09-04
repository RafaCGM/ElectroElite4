from BancoDados.models import *
from django.contrib import admin

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    ...

admin.site.register(Clientes, ClienteAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(CategoriaProduto, CategoriaAdmin)

class PagamentoAdmin(admin.ModelAdmin):
    ...

admin.site.register(MetodoPagamento, PagamentoAdmin)

class PedidosAdmin(admin.ModelAdmin):
    ...

admin.site.register(Pedidos, PedidosAdmin)

class ProdutosAdmin(admin.ModelAdmin):
    ...

admin.site.register(Produtos, ProdutosAdmin)

class ItensAdmin(admin.ModelAdmin):
    ...

admin.site.register(ItensPedidos, ItensAdmin)
