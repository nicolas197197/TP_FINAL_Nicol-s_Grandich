from django.urls import path

from app_futbolistas import views



urlpatterns = [
path('in_futbolistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_futbolistas),
path('basquet', views.FutbolListView.as_view(), name='futbol-list'),
path('basquet/add/', views.FutbolCreateView.as_view(), name='futbol-add'),
path('basquet/<int:pk>/detail', views.FutbolDetailView.as_view(), name='futbol-detail'),
path('basquet/<int:pk>/update', views.FutbolUpdateView.as_view(), name='futbol-update'),
path('basquet/<int:pk>/delete', views.FutbolDeleteView.as_view(), name='futbol-delete'),
]