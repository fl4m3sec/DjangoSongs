from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    popularidad = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    class Meta:
        db_table = 'cancion'
        verbose_name = 'Cancion'
        verbose_name_plural = 'Canciones'

    def str(self):
        return f'{self.titulo} - {self.artista}'