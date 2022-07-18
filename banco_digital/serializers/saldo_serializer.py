
from rest_framework import serializers

from banco_digital.models.usuario import Usuario


class SaldoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ("cod_conta", "saldo_atual")