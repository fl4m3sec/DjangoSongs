from django.contrib import admin
from .models import Cancion

# Register your models here.

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'artista', 'popularidad')
    search_fields = ('id', 'titulo', 'artista', 'popularidad')