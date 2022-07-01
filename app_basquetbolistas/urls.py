from django.urls import path

from app_basquetbolistas import views


urlpatterns = [
path('in_basquetbolistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_basquetbolistas),
#path('basquetbolistas/', views.basquetbolistas, name='basquetbolistas'),
path('basquet-django-forms', views.basquet_forms_django, name='BasquetDjangoForms'),
path('basquet', views.BasquetListView.as_view(), name='basquet-list'),
path('basquet/add/', views.BasquetCreateView.as_view(), name='basquet-add'),
path('basquet/<int:pk>/detail', views.BasquetDetailView.as_view(), name='basquet-detail'),
path('basquet/<int:pk>/update', views.BasquetUpdateView.as_view(), name='basquet-update'),
path('basquet/<int:pk>/delete', views.BasquetDeleteView.as_view(), name='basquet-delete'),
]