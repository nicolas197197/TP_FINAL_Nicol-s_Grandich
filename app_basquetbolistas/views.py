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


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BasquetListView(ListView):
    model = Basquet
    template_name = "app_basquetbolistas/basquet_list.html"


class BasquetDetailView(DetailView):
    model = Basquet
    template_name = "app_basquetbolistas/basquet_detail.html"


class BasquetCreateView(CreateView):
    model = Basquet
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('basquet-list')
    fields = ['nombre', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class BasquetUpdateView(UpdateView):
    model = Basquet
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('basquet-list')
    fields = ['nombre', 'numeroDeSocio', 'fechaDeIngreso', 'email']


class BasquetDeleteView(DeleteView):
    model = Basquet
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('basquet-list')    