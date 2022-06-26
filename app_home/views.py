from django.shortcuts import render
from app_futbolistas.models import Futbol
from app_basquetbolistas.models import Basquet
from app_tenistas.models import Tenis
from django.db.models import Q

def index(request):
    return render(request,"app_home/home.html")

def search(request):
    context_dict = dict()
    if request.GET['all_search_futbolistas']:
        search_param = request.GET['all_search_futbolistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        futbol = Futbol.objects.filter(query)
        context_dict = {
            'futbol': futbol
        }

    elif request.GET['all_search_basquetbolistas']:
        search_param = request.GET['all_search_basquetbolistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        basquet = Basquet.objects.filter(query)
        context_dict = {
            'basquet': basquet
        }

    elif request.GET['all_search_tenistas']:
        search_param = request.GET['all_search_tenistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        tenis = Tenis.objects.filter(query)
        context_dict = {
            'tenis': tenis
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_home/home.html",
    )            