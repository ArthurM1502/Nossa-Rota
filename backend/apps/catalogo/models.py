from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    class Meta:
        ordering = ['nome']
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'uf'], name='cidade_nome_uf_unico'
            )
        ]

    def __str__(self):
        return f'{self.nome}/{self.uf}'


class Unidade(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.sigla


class Categoria(models.Model):
    class Tipo(models.TextChoices):
        MATERIAL = 'material', 'Material'
        SERVICO = 'servico', 'Serviço'
        SOBRA = 'sobra', 'Sobra'

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=Tipo.choices)

    class Meta:
        ordering = ['tipo', 'nome']
        constraints = [
            models.UniqueConstraint(
                fields=['nome', 'tipo'], name='categoria_nome_tipo_unico'
            )
        ]

    def __str__(self):
        return f'{self.nome} ({self.get_tipo_display()})'


class ModalidadeEntrega(models.Model):
        nome = models.CharField(max_length=50, unique=True)

        class Meta:
            ordering = ['nome']

        def __str__(self):
            return self.nome