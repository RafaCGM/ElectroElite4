from django.shortcuts import render
from .forms import *

def view_cadcliente(request):
    form = RegisterCliente()
    return render(request, 'cadcliente.html', {'form': form})
def view_create_cliente(request):
    if request.POST:
        form = RegisterCliente(request.POST)
        form.save()
    else:
        form = RegisterCliente()
   
    return render(request, 'cadcliente.html', {'form': form, 'ok':'FUNCIONOU'})

def view_cadcategoria(request):
    form = RegisterCategoria()
    return render(request, 'cadcategoria.html', {'form': form})
def view_create_categoria(request):
    if request.POST:
        form = RegisterCategoria(request.POST)
        form.save()
    else:
        form = RegisterCategoria()
   
    return render(request, 'cadcategoria.html', {'form': form, 'ok':'FUNCIONOU'})

def view_caditenspedidos(request):
    form = RegisterItensPedidos()
    return render(request, 'caditenspedidos.html', {'form': form})
def view_create_itenspedidos(request):
    if request.POST:
        form = RegisterItensPedidos(request.POST)
        form.save()
    else:
        form = RegisterItensPedidos()
        
    return render(request, 'caditenspedidos.html', {'form': form, 'ok':'FUNCIONOU'})

def view_cadmetpagamento(request):
    form = RegisterMetPagamento()
    return render(request, 'cadmetpagamento.html', {'form': form})
def view_create_metpagamento(request):
    if request.POST:
        form = RegisterMetPagamento(request.POST)
        form.save()
    else:
        form = RegisterMetPagamento()
   
    return render(request, 'cadmetpagamento.html', {'form': form, 'ok':'FUNCIONOU'})

def view_cadpedido(request):
    form = RegisterPedidos()
    return render(request, 'cadpedido.html', {'form': form})
def view_create_pedido(request):
    if request.POST:
        form = RegisterPedidos(request.POST)
        form.save()
    else:
        form = RegisterPedidos()
        
    return render(request, 'cadpedido.html', {'form': form, 'ok':'FUNCIONOU'})

def view_cadproduto(request):
    form = RegisterProdutos()
    return render(request, 'cadproduto.html', {'form': form})
def view_create_produto(request):
    if request.POST:
        form = RegisterProdutos(request.POST)
        form.save()
    else:
        form = RegisterProdutos()
   
    return render(request, 'cadproduto.html', {'form': form, 'ok':'FUNCIONOU'})