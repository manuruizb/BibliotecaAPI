from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fileds = ('__all__')
    search_fields = ('__all__')#('valor', 'tipoDePropiedad')
    ordering_fields = ('__all__')