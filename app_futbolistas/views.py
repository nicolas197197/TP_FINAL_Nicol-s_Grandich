from django.shortcuts import render
from app_futbolistas.models import Futbol


def in_futbolistas(request, nombre: str, numeroDeSocio: int, fechaDeIngreso: str, email: str):
    futbol = Futbol(nombre=nombre, numeroDeSocio=numeroDeSocio, fechaDeIngreso=fechaDeIngreso, email=email)
    futbol.save() # save into the DB

    context_dict = {
        'futbol': futbol
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_futbolistas/in_futbolistas.html"
    )

def futbolistas(request):
    futbol = Futbol.objects.all()

    context_dict = {
        'futbol': futbol
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_futbolistas/futbolistas.html"
    )