from django.urls import path

from app_basquetbolistas import views


urlpatterns = [
path('in_basquetbolistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_basquetbolistas),
path('basquetbolistas/', views.basquetbolistas, name='basquetbolistas'),

]