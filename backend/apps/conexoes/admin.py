from django.contrib import admin

from .models import Conexao


@admin.register(Conexao)
class ConexaoAdmin(admin.ModelAdmin):
    list_display = ['interessado', 'anuncio', 'servico', 'criado_em']
    list_filter = ['criado_em']
    search_fields = ['interessado__nome_exibicao', 'mensagem']
    readonly_fields = ['criado_em']
    raw_id_fields = ['interessado', 'anuncio', 'servico']