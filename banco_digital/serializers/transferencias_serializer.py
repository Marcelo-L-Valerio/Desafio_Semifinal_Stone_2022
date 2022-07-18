
from rest_framework import serializers

from banco_digital.models.transferencias import Transferencias
from banco_digital.models.usuario import Usuario

class TransferenciasSerializer(serializers.ModelSerializer):

    cod_transferencia = serializers.CharField(min_length=15)
    conta_origem = serializers.CharField(min_length=10)
    conta_destino = serializers.CharField(min_length=10)

    class Meta:
        model = Transferencias
        fields = ("id", "cod_transferencia", "conta_origem", "conta_destino", "valor", "data_transferencia")

    def validate_conta_destino(self, conta_destino):
        if not Usuario.objects.filter(cod_conta=conta_destino):
            raise serializers.ValidationError({'conta_destino': 'Conta de destino não existe'})
        return conta_destino

    def validate_conta_origem(self, conta_origem):
        if not Usuario.objects.filter(cod_conta=conta_origem):
            raise serializers.ValidationError({'conta_origem': 'Conta de origem não existe'})
        return conta_origem

    def validate_cod_transferencia(self, cod_transferencia):
        if Transferencias.objects.filter(cod_transferencia=cod_transferencia):
            raise serializers.ValidationError({'cod_transferencia': 'Codigo de transferencia já existente'})
        return cod_transferencia

    def create(self, validated_data):
        usuario_origem = Usuario.objects.get(cod_conta=self.data['conta_origem'])
        saldo_origem = usuario_origem.saldo_atual #acessa o saldo atual da conta de origem
        usuario_destino = Usuario.objects.get(cod_conta=self.data['conta_destino'])
        saldo_destino = usuario_destino.saldo_atual #acessa o saldo atual da conta de destino
        novo_saldo_origem = saldo_origem - round(self.data['valor'], 2) #faz as contas dos saldos, arredondando
        novo_saldo_destino = saldo_destino + round(self.data['valor'], 2) # o valor da transferencia para duas casas decimais
        if novo_saldo_origem < 0:
            usuario_origem.save()
            usuario_destino.save()
            raise serializers.ValidationError({'conta_origem': 'Saldo insulficiente'})
        elif usuario_origem.cod_conta == usuario_destino.cod_conta:
            usuario_origem.save()
            usuario_destino.save()
            raise serializers.ValidationError({'conta_destino': 'Contas origem e destino são iguais'})
        else:
            usuario_origem.saldo_atual = novo_saldo_origem
            usuario_origem.save()
            usuario_destino.saldo_atual = novo_saldo_destino
            usuario_destino.save()

        return super().create(validated_data)