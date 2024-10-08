# Generated by Django 5.0.7 on 2024-07-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nomeCategoria', models.CharField(max_length=70)),
                ('descricaoCategoria', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPagamento',
            fields=[
                ('idMetodoPagamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nomeMetodo', models.CharField(max_length=70)),
                ('descricaoMetodo', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nomeUsuario', models.CharField(max_length=300)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=300)),
                ('senha', models.CharField(max_length=300)),
                ('endereco', models.CharField(max_length=300)),
            ],
        ),
    ]
