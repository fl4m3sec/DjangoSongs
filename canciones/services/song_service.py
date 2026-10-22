from django.db.models import Q
from django.shortcuts import get_object_or_404

from canciones.models import Cancion

def obtener_todas(busqueda=''):
    """Muestrame todas la canciones, primero las mas populares"""
    canciones = Cancion.objects.all()
    if busqueda:
        canciones = canciones.filter(
            Q(titulo__icontains=busqueda) | Q(artista__icontains=busqueda)
        )
    return canciones.order_by('-popularidad', 'titulo')


def obtener_por_id(id):
    """Devuelve una cancion o lanza un error 404 si no existe"""
    return get_object_or_404(Cancion, pk=id)

def crear_cancion(datos):
    """Crea un cancion a partir de un diccionario con titulo, artista y popularidad"""
    return Cancion.objects.create(
        titulo=datos['titulo'],
        artista=datos['artista'],
        popularidad=datos['popularidad']
    )

def actualizar_cancion(id, datos):
    """Actualiza los datos de la cancion existente"""
    cancion = get_object_or_404(Cancion, pk=id)
    cancion.titulo = datos['titulo']
    cancion.artista = datos['artista']
    cancion.popularidad = datos['popularidad']
    cancion.save()
    return cancion

def eliminar_cancion(id):
    """Elimina los datos de la cancion existente"""
    cancion = get_object_or_404(Cancion, pk=id)
    cancion.delete()









