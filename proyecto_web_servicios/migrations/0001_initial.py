# Generated by Django 3.1.5 on 2021-03-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='charfield', max_length=40)),
                ('apellido', models.CharField(default='charfield', max_length=40)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(default='charfield', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='charfield', max_length=40)),
                ('apellido', models.CharField(default='charfield', max_length=40)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(default='charfield', max_length=50)),
                ('email', models.EmailField(default='charfield', max_length=254)),
                ('matricula', models.BooleanField(default='charfield')),
                ('servicio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='charfield', max_length=100)),
                ('imagen', models.ImageField(upload_to='varios')),
            ],
        ),
    ]
