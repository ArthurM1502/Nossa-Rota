from django.db import models


class Etapa(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    ordem = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    conexao = models.ForeignKey(
        'conexoes.Conexao',
        on_delete=models.PROTECT,
        related_name='pedidos'
    )
    empresa = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.PROTECT,
        related_name='pedidos_organizados',
    )
    responsavel_atual = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.PROTECT,
        related_name='pedidos_em_execucao',
    )
    etapa_atual = models.ForeignKey(
        'Etapa',
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    prazo_entrega = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['prazo_entrega']

    def __str__(self):
        return self.titulo


class Peca(models.Model):
    pedido = models.ForeignKey(
        'Pedido',
        on_delete=models.CASCADE,
        related_name='pecas',
    )
    descricao = models.CharField(max_length=150)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.descricao} ({self.quantidade})'


class HistoricoEtapa(models.Model):
    pedido = models.ForeignKey(
        'Pedido',
        on_delete=models.PROTECT,
        related_name='historico',
    )
    etapa_origem = models.ForeignKey(
        'Etapa',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True,
    )
    etapa_destino = models.ForeignKey(
        'Etapa',
        on_delete=models.PROTECT,
        related_name='+'
    )
    movido_por = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.PROTECT,
        related_name='+'
    )
    responsavel = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.PROTECT,
        related_name='+',
    )
    observacao = models.TextField(blank=True)
    em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['em']

    def __str__(self):
        return f'{self.pedido} -> {self.etapa_destino}'