from django.shortcuts import render
from app_futbolistas.models import Futbol
from app_futbolistas.forms import FutbolForm


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

def futbol_forms_django(request):
    if request.method == 'POST':
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol = Futbol(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            futbol.save()

            futbol = Futbol.objects.all()
            context_dict = {
                'futbol': futbol
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_futbolistas/futbolistas.html"
            )

    futbol_form = FutbolForm(request.POST)
    context_dict = {
        'futbol_form': futbol_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_futbolistas/futbol_forms_django.html'
    )