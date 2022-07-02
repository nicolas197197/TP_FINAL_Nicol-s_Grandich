from django.shortcuts import render
from app_futbolistas.models import Futbol
from app_futbolistas.forms import FutbolForm
from django.forms.models import model_to_dict


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


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class FutbolListView(ListView):
    model = Futbol
    template_name = "app_futbolistas/futbol_list.html"


class FutbolDetailView(DetailView):
    model = Futbol
    template_name = "app_futbolistas/futbol_detail.html"


class FutbolCreateView(CreateView):
    model = Futbol
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('futbol-list')
    fields = ['nombre', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class FutbolUpdateView(UpdateView):
    model = Futbol
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('futbol-list')
    fields = ['nombre', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class FutbolDeleteView(DeleteView):
    model = Futbol
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('futbol-list')    