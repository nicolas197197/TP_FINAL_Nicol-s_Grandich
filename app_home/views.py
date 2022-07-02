from django.shortcuts import render
from app_futbolistas.models import Futbol
from app_basquetbolistas.models import Basquet
from app_tenistas.models import Tenis
from django.db.models import Q
from app_user.models import Avatar
from app_user.forms import AvatarForm

def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="app_home/home.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


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

