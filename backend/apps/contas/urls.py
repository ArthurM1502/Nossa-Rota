from django.urls import path

from .views import CadastroView, PerfilView


urlpatterns = [
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('perfil/', PerfilView.as_view(), name='perfil')
]