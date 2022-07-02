from django.urls import path

from app_tenistas import views


urlpatterns = [
path('in_tenistas/<str:nombre>/<int:numeroDeSocio>/<fechaDeIngreso>/<str:email>', views.in_tenistas),
path('basquet', views.TenisListView.as_view(), name='tenis-list'),
path('basquet/add/', views.TenisCreateView.as_view(), name='tenis-add'),
path('basquet/<int:pk>/detail', views.TenisDetailView.as_view(), name='tenis-detail'),
path('basquet/<int:pk>/update', views.TenisUpdateView.as_view(), name='tenis-update'),
path('basquet/<int:pk>/delete', views.TenisDeleteView.as_view(), name='tenis-delete'),
]