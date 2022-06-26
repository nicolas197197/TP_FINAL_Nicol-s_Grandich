from django.shortcuts import render
from app_basquetbolistas.models import Basquet
from app_basquetbolistas.forms import BasquetForm

def in_basquetbolistas(request, nombre: str, numeroDeSocio: int, fechaDeIngreso: str, email: str):
    basquet = Basquet(nombre=nombre, numeroDeSocio=numeroDeSocio, fechaDeIngreso=fechaDeIngreso, email=email)
    basquet.save() # save into the DB

    context_dict = {
        'basquet': basquet
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_basquetbolistas/in_basquetbolistas.html"
    )

def basquetbolistas(request):
    basquet = Basquet.objects.all()

    context_dict = {
        'basquet': basquet
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_basquetbolistas/basquetbolistas.html"
    )

def basquet_forms_django(request):
    if request.method == 'POST':
        basquet_form = BasquetForm(request.POST)
        if basquet_form.is_valid():
            data = basquet_form.cleaned_data
            basquet = Basquet(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            basquet.save()

            basquet = Basquet.objects.all()
            context_dict = {
                'basquet': basquet
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_basquetbolistas/basquetbolistas.html"
            )

    basquet_form = BasquetForm(request.POST)
    context_dict = {
        'basquet_form': basquet_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_basquetbolistas/basquet_forms_django.html'
    )
