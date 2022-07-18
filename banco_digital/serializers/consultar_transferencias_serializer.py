
from rest_framework import serializers

from banco_digital.models.transferencias import Transferencias

class ConsultarTransferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transferencias
        fields = ("__all__")

    