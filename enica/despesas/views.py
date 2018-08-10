from django.shortcuts import render, get_object_or_404
from .models import Despesa, Categoria,Parcela
from .serializers import DespesaSerializer,CategoriaSerializer,ParcelaSerializer
from rest_framework import generics

# Create your views here.

class DespesaListCreate(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ParcelaListCreate(generics.ListCreateAPIView):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj