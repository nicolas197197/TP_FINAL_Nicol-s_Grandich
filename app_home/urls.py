from django.urls import path

from app_home import views


urlpatterns = [
path('', views.index, name=''),
path('search', views.search, name='Search'),


]