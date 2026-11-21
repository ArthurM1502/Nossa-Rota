from django.conf import settings
from django.db import models


class Perfil(models.Model):
    class Tipo(models.TextChoices):
        COMERCIO = 'comercio', 'Comércio'
        FACCAO = 'faccao', 'Facção'
        EMPRESA = 'empresa', 'Empresa'

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    nome_exibicao = models.CharField(max_length=150)
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    cidade = models.ForeignKey(
        'catalogo.Cidade',
        on_delete=models.PROTECT,
        related_name='perfis'
    )
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14, blank=True)


    class Meta:
        ordering = ['nome_exibicao']
        constraints = [
            models.UniqueConstraint(
                fields=['cnpj'],
                condition=~models.Q(cnpj=''),
                name='perfil_cnpj_unico_quando_preenchido'
            )
        ]

    def __str__(self):
        return f'{self.nome_exibicao} ({self.get_tipo_display()})'