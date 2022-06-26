from django.shortcuts import render
from app_basquetbolistas.models import Basquet

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
