from django.urls import path

from app_tenistas import views


urlpatterns = [
path('in_tenistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_tenistas),
path('tenistas/', views.tenistas, name='tenistas'),
path('tenis-django-forms', views.tenis_forms_django, name='TenisDjangoForms'),

]