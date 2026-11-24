from django.contrib import admin

from .models import Anuncio, Servico


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'anunciante', 'preco', 'ativo']
    list_filter = ['ativo', 'categoria__tipo', 'categoria']
    search_fields = ['titulo', 'descricao']
    filter_horizontal = ['modalidades_entrega']
    readonly_fields = ['criado_em']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'prestador', 'preco', 'ativo']
    list_filter = ['ativo', 'categoria']
    search_fields = ['descricao']
    readonly_fields = ['criado_em']