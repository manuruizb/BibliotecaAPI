from rest_framework import serializers
from .models import *

class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'