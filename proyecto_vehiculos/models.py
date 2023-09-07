from django.db import models

class Vehiculo(models.Model):
    MARCAS_CHOICES = [
        ('fiat', 'Fiat'),
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('chevrolet', 'Chevrolet'),
    ]

    marca = models.CharField(max_length=250, choices=MARCAS_CHOICES, blank=True, default='Ford')

    CATEGORIA_VEHICULOS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')    
    ]
    categoria = models.CharField(max_length=200, choices=CATEGORIA_VEHICULOS, blank=True, default='Particular')
    
    modelo= models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.FloatField(max_length=20)
    fecha_de_creacion = models.DateField(auto_now=True)
    fecha_de_modificacion = models.DateField(auto_now=True)
    
    
    class Meta:
        ordering = ["marca"]
        
    def get_absolute_url(self):
        return reverse('vehiculo', args=[str(self.id)])
    
    def __str__(self):
        return f"modelo: {self.modelo}"
    

    
