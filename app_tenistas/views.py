from django.shortcuts import render
from app_tenistas.models import Tenis


def in_tenistas(request, nombre: str, numeroDeSocio: int, fechaDeIngreso: str, email: str):
    tenis = Tenis(nombre=nombre, numeroDeSocio=numeroDeSocio, fechaDeIngreso=fechaDeIngreso, email=email)
    tenis.save() # save into the DB

    context_dict = {
        'tenis': tenis
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_tenistas/in_tenistas.html"
    )

def tenistas(request):
    tenis = Tenis.objects.all()

    context_dict = {
        'tenis': tenis
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_tenistas/tenistas.html"
    )