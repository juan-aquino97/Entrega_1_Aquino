# Generated by Django 4.1.2 on 2022-11-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=9, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
            ],
        ),
    ]
