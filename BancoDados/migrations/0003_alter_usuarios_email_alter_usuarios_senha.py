# Generated by Django 5.0.7 on 2024-08-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BancoDados', '0002_alter_categoriaproduto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.CharField(default='user@gmail.com', max_length=300),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='senha',
            field=models.CharField(default='123', max_length=300),
        ),
    ]
