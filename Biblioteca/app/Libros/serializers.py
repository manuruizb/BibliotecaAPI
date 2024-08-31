from rest_framework import serializers
from .models import *

class LibrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'