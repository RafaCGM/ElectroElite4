# Generated by Django 5.0.7 on 2024-07-29 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoDados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaproduto',
            options={'verbose_name_plural': 'Categoria de Produtos'},
        ),
        migrations.AlterModelOptions(
            name='metodopagamento',
            options={'verbose_name_plural': 'Metodos de Pagamento'},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='categoriaproduto',
            name='idCategoria',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='idUsuario',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('idPedido', models.BigAutoField(primary_key=True, serialize=False)),
                ('DataEmissao', models.DateField(help_text='Formato <em>yyyy-MM-DD</em>', null=True)),
                ('StatusPedido', models.CharField(max_length=45)),
                ('MetodoPagamento_idMetodoPagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BancoDados.metodopagamento')),
                ('Usuarios_idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BancoDados.usuarios')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('idProduto', models.BigAutoField(primary_key=True, serialize=False)),
                ('NomeProduto', models.CharField(max_length=200)),
                ('Preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Descricao', models.CharField(max_length=500, null=True)),
                ('Estoque', models.IntegerField()),
                ('CategoriaProduto_idCategoriaProduto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BancoDados.categoriaproduto')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='ItensPedidos',
            fields=[
                ('idItensPedidos', models.BigAutoField(primary_key=True, serialize=False)),
                ('Quantidade', models.IntegerField()),
                ('PrecoTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Pedidos_idPedidos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BancoDados.pedidos')),
                ('Produto_idProduto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BancoDados.produtos')),
            ],
            options={
                'verbose_name_plural': 'Itens Pedidos',
            },
        ),
    ]
