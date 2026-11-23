from django.db import models


class Anuncio(models.Model):
    anunciante = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.CASCADE,
        related_name='anuncios',
    )
    categoria = models.ForeignKey(
        'catalogo.Categoria',
        on_delete=models.PROTECT,
        related_name='anuncios',
        limit_choices_to={'tipo__in': ['material', 'sobra']},
    )
    unidade = models.ForeignKey(
        'catalogo.Unidade',
        on_delete=models.PROTECT,
        related_name='anuncios',
        null=True,
        blank=True,
    )
    modalidades_entrega = models.ManyToManyField(
        'catalogo.ModalidadeEntrega',
        related_name='anuncios',
        blank=True,
    )
    prazo_entrega_dias = models.PositiveSmallIntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_minima = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_disponivel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo


class Servico(models.Model):
    prestador = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.CASCADE,
        related_name='servicos',
    )
    categoria = models.ForeignKey(
        'catalogo.Categoria',
        on_delete=models.PROTECT,
        related_name='servicos',
        limit_choices_to={'tipo': 'servico'},
    )
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criados_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criados_em']

    def __str__(self):
        return f'{self.categoria.nome} - {self.prestador.nome_exibicao}'