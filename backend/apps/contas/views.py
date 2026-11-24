from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .models import Perfil
from .serializers import CadastroSerializer, PerfilSerializer


class CadastroView(generics.CreateAPIView):
    serializer_class = CadastroSerializer
    permission_classes = [permissions.AllowAny]


class PerfilView(generics.RetrieveUpdateAPIView):
    serializer_class = PerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            Perfil,
            usuario=self.request.user,
        )