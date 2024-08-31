from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class LibrosViewset(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializers

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('idStatus__status', 'titulo', 'autor', 'fecha_publicacion', 'genero')#('valor', 'tipoDePropiedad')
    ordering_fields = ('__all__')