from django.shortcuts import render
from core.serializers import ClienteSerializer
from rest_framwork import viewsets
from .models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.object.all()
    serializer_class = ClienteSerializer

