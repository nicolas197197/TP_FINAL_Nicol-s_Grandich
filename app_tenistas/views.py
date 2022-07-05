from django.shortcuts import render
from app_tenistas.models import Tenis
from app_tenistas.forms import TenisForm


def in_tenistas(request, nombre: str, apellido: str, numeroDeSocio: int, fechaDeIngreso: str, email: str):
    tenis = Tenis(nombre=nombre, apellido=apellido, numeroDeSocio=numeroDeSocio, fechaDeIngreso=fechaDeIngreso, email=email)
    tenis.save() # save into the DB

    context_dict = {
        'tenis': tenis
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_tenistas/in_tenistas.html"
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class TenisListView(ListView):
    model = Tenis
    template_name = "app_tenistas/tenis_list.html"


class TenisDetailView(DetailView):
    model = Tenis
    template_name = "app_tenistas/tenis_detail.html"


class TenisCreateView(CreateView):
    model = Tenis
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('tenis-list')
    fields = ['nombre', 'apellido', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class TenisUpdateView(UpdateView):
    model = Tenis
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('tenis-list')
    fields = ['nombre', 'apellido', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class TenisDeleteView(DeleteView):
    model = Tenis
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('tenis-list')    