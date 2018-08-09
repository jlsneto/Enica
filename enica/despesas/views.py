from django.shortcuts import render
from .models import Despesa
from .serializers import DespesaSerializer
from rest_framework import generics

# Create your views here.

class DespesaListCreate(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer