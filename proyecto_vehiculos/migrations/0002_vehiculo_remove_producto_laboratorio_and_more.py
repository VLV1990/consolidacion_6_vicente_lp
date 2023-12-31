# Generated by Django 4.2.5 on 2023-09-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, choices=[('fiat', 'Fiat'), ('toyota', 'Toyota'), ('ford', 'Ford'), ('chevrolet', 'Chevrolet')], default='Ford', max_length=250)),
                ('categoria', models.CharField(blank=True, choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='Particular', max_length=200)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serial_motor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio', models.FloatField(max_length=20)),
                ('fecha_de_creacion', models.DateField(auto_now=True)),
                ('fecha_de_modificacion', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['marca'],
            },
        ),
        migrations.RemoveField(
            model_name='producto',
            name='laboratorio',
        ),
        migrations.DeleteModel(
            name='DirectorGeneral',
        ),
        migrations.DeleteModel(
            name='Laboratorio',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
