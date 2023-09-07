from django.contrib import admin
from .models import Vehiculo


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id','marca','modelo','serial_carroceria','serial_motor','categoria','precio')
    list_filter = ('fecha_de_creacion', 'marca', 'precio')  # Una tupla con tres elementos
    ordering = ['marca']

    
admin.site.register(Vehiculo, VehiculoAdmin)



