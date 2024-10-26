# Generated by Django 5.0.7 on 2024-08-31 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoDados', '0004_alter_usuarios_email_alter_usuarios_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idCliente', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomeCliente', models.CharField(max_length=300)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=300)),
                ('endereco', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='Usuarios_idUsuario',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='Clientes_idCliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='BancoDados.clientes'),
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
