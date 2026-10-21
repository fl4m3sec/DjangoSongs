from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nueva/', views.create, name='cancion_create'),
    path('editar/<int:id>/', views.update, name='cancion_update'),
    path('eliminar/<int:id>/', views.delete, name='cancion_delete'),
]