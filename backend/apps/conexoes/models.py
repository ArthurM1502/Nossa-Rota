from django.db import models


class Conexao(models.Model):
    interessado = models.ForeignKey(
        'contas.Perfil',
        on_delete=models.CASCADE,
        related_name='conexoes',
    )
    anuncio = models.ForeignKey(
        'ofertas.Anuncio',
        on_delete=models.CASCADE,
        related_name='conexoes',
        null=True,
        blank=True,
    )
    servico = models.ForeignKey(
        'ofertas.Servico',
        on_delete=models.CASCADE,
        related_name='conexoes',
        null=True,
        blank=True,
    )
    mensagem = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(anuncio__isnull=False, servico__isnull=True) | models.Q(anuncio__isnull=True, servico__isnull=False)
                ),
                name='conexao_um_alvo_apenas',
            )
        ]

    def __str__(self):
        alvo = self.anuncio or self.servico
        return f'{self.interessado.nome_exibicao} -> {alvo}'