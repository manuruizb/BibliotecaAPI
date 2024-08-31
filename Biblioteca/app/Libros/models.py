from django.db import models
from ..Status.models import *


'''
Una biblioteca local está digitalizando su catálogo de libros y quiere crear una API que permita a los usuarios buscar y ver detalles de los libros disponibles.
La API deberá gestionar información básica sobre los libros, como el título, autor, fecha de publicación, género, y si están disponibles o prestados.
'''

class Libros(models.Model):
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False)
    titulo = models.CharField(verbose_name='Titulo', max_length=100, blank=False, null=False)
    autor = models.CharField(verbose_name='Autor', max_length=50, blank=False, null=False)
    fecha_publicacion = models.DateTimeField(verbose_name='Fecha Publicacion', blank=False, null=False)
    genero = models.CharField(verbose_name='Genero', max_length=30, blank=False, null=False)
    
    def __str__(self):
        return f'{self.titulo} - {self.genero} - {self.autor} - {self.fecha_publicacion}'
   