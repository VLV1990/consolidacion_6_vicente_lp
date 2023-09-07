from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.http import HttpResponseRedirect

def v_list(request):
    
    if 'numveces' in request.session:
        num = request.session["numveces"] 
    else:
        num = 0
    
    
    request.session["numveces"] = num + 1 

    context = {
        'numveces': request.session["numveces"],
        'labos': Vehiculo.objects.all()
    }



    return render(request, 'list.html', context)

def v_create(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = VehiculoForm(datos)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect("/")
    
    
    context = {
        'formulario': VehiculoForm()
    }
    return render(request, 'create.html', context)



