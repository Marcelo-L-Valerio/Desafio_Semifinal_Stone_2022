
from django.db import models


class Transferencias(models.Model):
    cod_transferencia = models.CharField(max_length=15)
    conta_origem = models.CharField(max_length=10)
    conta_destino = models.CharField(max_length=10)
    valor = models.FloatField(default=0.0)
    data_transferencia = models.DateField()

    def __str__(self) -> str:
        return self.nome

    