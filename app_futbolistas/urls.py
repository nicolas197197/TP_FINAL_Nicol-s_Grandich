from django.urls import path

from app_futbolistas import views


urlpatterns = [
path('in_futbolistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_futbolistas),


]