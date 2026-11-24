from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction

from rest_framework import serializers

from .models import Perfil


Usuario = get_user_model()


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [
            'id', 
            'nome_exibicao',
            'tipo',
            'cidade',
            'telefone',
            'cnpj',
        ]
        read_only_fields = ['id']


class CadastroSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )
    confirmar_senha = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'email',
            'password',
            'confirmar_senha',
            'perfil',
        ]
        read_only_fields = ['id']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmar_senha']:
            raise serializers.ValidationError({
                'confirmar_senha': 'As senhas informadas não coincidem.'
            })

        usuario = Usuario(
            username=attrs.get('username', ''),
            email=attrs.get('email', ''),
        )

        try:
            password_validation.validate_password(
                attrs['password'],
                user=usuario,
            )
        except DjangoValidationError as exc:
            raise serializers.ValidationError({
                'password': list(exc.messages)
            })

        return attrs


    @transaction.atomic
    def create(self, validate_data):
        dados_perfil = validate_data.pop('perfil')
        senha = validate_data.pop('password')
        validate_data.pop('confirmar_senha')

        usuario = Usuario.objects.create_user(
            password=senha,
            **validate_data,
        )

        Perfil.objects.create(
            usuario=usuario,
            **dados_perfil,
        )

        return usuario