from django.shortcuts import render
from app_tenistas.models import Tenis
from app_tenistas.forms import TenisForm


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

def tenis_forms_django(request):
    if request.method == 'POST':
        tenis_form = TenisForm(request.POST)
        if tenis_form.is_valid():
            data = tenis_form.cleaned_data
            tenis = Tenis(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            tenis.save()

            tenis = Tenis.objects.all()
            context_dict = {
                'tenis': tenis
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_tenistas/tenistas.html"
            )

    tenis_form = TenisForm(request.POST)
    context_dict = {
        'tenis_form': tenis_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_tenistas/tenis_forms_django.html'
    )
