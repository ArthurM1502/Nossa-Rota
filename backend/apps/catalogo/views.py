from rest_framework import viewsets

from .models import Categoria, Cidade, ModalidadeEntrega, Unidade
from .serializers import (
    CategoriaSerializer,
    CidadeSerializer, 
    ModalidadeEntregaSerializer, 
    UnidadeSerializer,
)


class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class UnidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer


class ModalidadeEntregaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ModalidadeEntrega.objects.all()
    serializer_class = ModalidadeEntregaSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer