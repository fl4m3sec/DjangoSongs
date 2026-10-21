from django.shortcuts import get_object_or_404

from canciones.models import Cancion

def obtener_todas():
    """Muestrame todas la canciones, primero las mas populares"""
    return Cancion.objects.all().order_by('-popularidad', 'titulo')

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









