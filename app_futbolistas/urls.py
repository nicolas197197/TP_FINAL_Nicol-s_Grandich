from django.urls import path

from app_futbolistas import views



urlpatterns = [
path('in_futbolistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_futbolistas),
path('futbolistas/', views.futbolistas, name='futbolistas'),
path('futbol-django-forms', views.futbol_forms_django, name='FutbolDjangoForms'),
path('futbol/<int:pk>/update', views.update_futbolista, name='UpdateFutbol'),
path('futbol/<int:pk>/delete', views.delete_futbolistas, name='DeleteFutbol'),

]