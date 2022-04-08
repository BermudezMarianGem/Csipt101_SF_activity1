from rest_framework import serializers
from . models import vehicls

class vehiclsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicls
        fields = ('name', 'description')