from django.db import models

# Create your models here.

class Clientes(models.Model):
    idCliente = models.BigAutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=300, null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=15,null=False)
    email = models.CharField(max_length=300, null=False)
    endereco = models.CharField(max_length=300, null=False)

    class Meta:
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return "CPF: " + self.cpf + " - Nome: " + self.nomeCliente

class CategoriaProduto(models.Model):
    idCategoria = models.BigAutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=70, null=False)
    descricaoCategoria = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name_plural = "Categoria de Produtos"
    
    def __str__(self):
        return self.nomeCategoria

class MetodoPagamento(models.Model):
    idMetodoPagamento = models.IntegerField(primary_key=True)
    nomeMetodo = models.CharField(max_length=70, null=False)
    descricaoMetodo = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name_plural = "Metodos de Pagamento"
    
    def __str__(self):
        return self.nomeMetodo

class Pedidos(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    Clientes_idCliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    DataEmissao = models.DateField(null=True,
                                    help_text="Formato <em>yyyy-MM-DD</em>")
    StatusPedido = models.CharField(max_length=45, null=False)
    MetodoPagamento_idMetodoPagamento = models.ForeignKey(MetodoPagamento, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Pedidos"
    
    def __str__(self):
        return "ID: " + str(self.idPedido) + " | Cliente: " + str(self.Clientes_idCliente) + " | Status: " + str(self.StatusPedido)

class Produtos(models.Model):
    idProduto = models.BigAutoField(primary_key=True)
    NomeProduto = models.CharField(max_length=200,null=False)
    Preco = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    Descricao = models.CharField(max_length=500,null=True)
    Estoque = models.IntegerField(null=False)
    CategoriaProduto_idCategoriaProduto = models.ForeignKey(CategoriaProduto, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Produtos"
    
    def __str__ (self):
        return self.NomeProduto + " | Estoque: " + str(self.Estoque)

class ItensPedidos(models.Model):
    idItensPedidos = models.BigAutoField(primary_key=True)
    Quantidade = models.IntegerField(null=False)
    PrecoTotal = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    Produto_idProduto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    Pedidos_idPedidos = models.ForeignKey(Pedidos, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Itens Pedidos"
    
    def __str__(self):
        return "ID: " + str(self.idItensPedidos)