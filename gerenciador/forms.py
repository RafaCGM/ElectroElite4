from django import forms
from BancoDados.models import *

class RegisterCategoria(forms.ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = '__all__'
        labels = {
                'idCategoria' : 'Identificação de Categoria',
                'nomeCategoria' : 'Nome da Categoria',
                'descricaoCategoria' : 'Descrição de categoria'
        }

        help_texts = {
            'nomeCategoria': 'Digite o nome da categoria.',
        }

        error_messages = {
            'nomeCategoria': {
                'required': 'Este campo não pode ser vazio.'
            },
        }

class RegisterCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        labels = {
                'idCliente' : 'Identificação do Cliente',
                'nomeCliente' : 'Nome e Sobrenome',
                'cpf' : 'CPF',
                'telefone' : 'Telefone',
                'email' : 'E-mail',
                'endereco' : 'Endereço'
        }

        help_texts = {
            'nomeCliente': 'Digite nome e sobrenome',
        }

        error_messages = {
            'nomeCliente': {
                'required': 'Este campo não pode ser vazio.'
            },'cpf': {
                'required': 'Este campo não pode ser vazio.'
            },'telefone': {
                'required': 'Este campo não pode ser vazio.'
            },'email': {
                'required': 'Este campo não pode ser vazio.'
            },'endereco': {
                'required': 'Este campo não pode ser vazio.'
            },
        }

class RegisterItensPedidos(forms.ModelForm):
    class Meta:
        model = ItensPedidos
        fields = '__all__'
        labels = {
                'idItensPedidos' : 'Identidicação dos Itens Pedidos',
                'Quantidade' : 'Quantidade dos itens',
                'PrecoTotal' : 'Preço total do pedido',
                'Produto_idProduto' : 'Identificação dos produtos',
                'Pedidos_idPedidos' : 'Identificação do Pedido'

        }

        help_texts = {

        }

        error_messages = {
            'idItensPedidos': {
                'required': 'Este campo não pode ser vazio.'
            },

            'Quantidade': {
                'required': 'Informe a quantidade de produtos comprados.'
            },

            'PrecoTotal': {
                'required': 'Informe o preço total da compra.'
            },

            'Produto_idProduto': {
                'required': 'Informe os produtos comprados.'
            },

            'Pedidos_idPedidos': {
                'required': 'Informe a identificação deste pedido.'
            }

        }

class RegisterMetPagamento(forms.ModelForm):
    class Meta:
        model = MetodoPagamento
        fields = '__all__'
        labels = {
            'idMetodoPagamento' : 'ID: ',
            'nomeMetodo': 'Nome do método: ',
            'descricaoMetodo': 'Descrição: ',
        }

        help_texts = {
            'nomeMetodo': 'Digite o nome do método de pagamento.',
            'descricaoMetodo': 'Descrição do método.'
        }

        error_messages = {
            'nomeMetodo': {
                'required': 'Este campo não pode ser vazio.'
            },
            'descricaoMetodo': {
                'required': 'Descrição inválida'
            }
        }

class RegisterPedidos(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'
        labels = {
                'idPedido' : 'Identidicação do Pedido',
                'Usuarios_idUsuario' : 'Identificação do Usuário',
                'DataEmissao' : 'Data de emissão do pedido',
                'StatusPedido' : 'Situação do pedido',
                'MetodoPagamento_idMetodoPagamento' : 'Método de pagamento'
        }

        help_texts = {
        }

        error_messages = {
            'Usuarios_idUsuario': {
                'required': 'Este campo não pode ser vazio.'
            },

            'MetodoPagamento_idMetodoPagamento': {
                'required': 'Selecione um método de pagamento'
            }
        }

class RegisterProdutos(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = '__all__'
        labels = {
            'idProduto' : 'Identificação do Produto',
            'NomeProduto' : 'Nome do Produto',
            'Preco' : 'Preço',
            'Descricao' : 'Descrição do Produto',
            'Estoque' : 'Quantidade em estoque',
            'CategoriaProduto_idCategoriaProduto' : 'Categoria'

        }

        help_texts = {
            'NomeProduto': 'Digite o nome do produto.',
            'Preço': 'Quanto custará esse produto?',
            'Descricao' : 'Descreva as caracteristicas desse produto'
        }

        error_messages = {
            'nomeProduto': {
                'required': 'Este campo não pode ser vazio.'
            },
            'Preço': {
                'required': 'Defina um preço, o valor não pode ser nulo.'
            }
        }
