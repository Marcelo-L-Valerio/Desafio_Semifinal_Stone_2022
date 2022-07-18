from django.db import models


class Usuario(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'
    USUARIO_CHOICES = [
        (PESSOA_FISICA, 'Fisica'),
        (PESSOA_JURIDICA, 'Juridica'),
    ]
    cod_conta = models.CharField(max_length=10)
    tipo = models.CharField(max_length = 2, choices = USUARIO_CHOICES, default = PESSOA_FISICA)
    cpf = models.CharField(max_length=11, null=True, unique=True)
    cnpj = models.CharField(max_length=14, null=True, unique=True)
    nome = models.CharField(max_length=140)
    email = models.CharField(max_length=200)
    saldo_atual = models.FloatField(default = 0)
    data_registro = models.DateField()

    def __str__(self) -> str:
        return self.nome