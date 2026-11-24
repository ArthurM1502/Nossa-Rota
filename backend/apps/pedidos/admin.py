from django.contrib import admin

from .models import Etapa, HistoricoEtapa, Peca, Pedido


class PecaInline(admin.TabularInline):
    model = Peca
    extra = 1

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['ordem', 'nome']
    ordering = ['ordem']


@admin.register(HistoricoEtapa)
class HistoricoEtapaAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'etapa_origem', 'etapa_destino', 'responsavel', 'movido_por', 'em']
    list_filter = ['etapa_destino']
    readonly_fields = ['em']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'empresa', 'responsavel_atual', 'etapa_atual', 'prazo_entrega']
    list_filter = ['etapa_atual', 'prazo_entrega']
    search_fields = ['titulo', 'descricao', 'empresa__nome_exibicao']
    readonly_fields = ['criado_em']
    raw_id_fields = ['conexao', 'empresa', 'responsavel_atual']
    inlines = [PecaInline]