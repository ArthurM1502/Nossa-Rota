from django.contrib import admin

from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome_exibicao', 'tipo', 'cidade', 'telefone']
    list_filter = ['tipo', 'cidade']
    search_fields = ['nome_exibicao', 'cnpj']
    raw_id_fields = ['usuario']
