from rest_framework import serializers

from .models import Categoria, Cidade, ModalidadeEntrega, Unidade


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'uf']


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = ['id', 'nome', 'sigla']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo']


class ModalidadeEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadeEntrega
        fields = ['id', 'nome']