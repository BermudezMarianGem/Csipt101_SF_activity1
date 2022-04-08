from django.shortcuts import render
from rest_framework import viewsets
from .serializers import vehiclsSerializer
from .models import vehicls
# Create your views here.

class vehiclsviewset(viewsets.ModelViewSet):
    query = vehicls.objects.all().order_by('name')
    serializer_class = vehiclsSerializer
