from django.contrib import admin

from .models import Categoria, Cidade, ModalidadeEntrega, Unidade


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    search_fields = ['nome']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo']
    list_filter = ['tipo']
    search_fields = ['nome']

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    search_fields = ['nome', 'sigla']

@admin.register(ModalidadeEntrega)
class ModalidadeEntregaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
