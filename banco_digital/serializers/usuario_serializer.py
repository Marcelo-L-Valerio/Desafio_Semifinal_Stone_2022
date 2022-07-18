
import re
from rest_framework import serializers
from banco_digital.models.usuario import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    nome = serializers.CharField(min_length=10)
    tipo = serializers.CharField(min_length=2)
    email = serializers.CharField(min_length=10)
    cod_conta = serializers.CharField(min_length=10)

    class Meta:
        model = Usuario
        fields = ('url', 'id', 'cod_conta', 'nome', 'tipo', 'cpf', 'cnpj', 'email', 'saldo_atual', 'data_registro')

    def validate(self, data):
        if (data.get("tipo") == 'PJ'):

            if (data.get("cnpj") == None):
                raise serializers.ValidationError({'Tipo': 'Se tipo igual a PJ o cnpj é obrigatorio'})

            elif not re.match(r'^([\s\d]+)$', data.get("cnpj")):
                raise serializers.ValidationError({'CNPJ': 'CNPJ deve ser numerico'})

        elif (data.get("tipo") == 'PF'):

            if (data.get("cpf") == None):
                raise serializers.ValidationError({'Se tipo igual a PF o cpf é obrigatorio'})

            elif not re.match(r'^([\s\d]+)$', data.get("cpf")):
                raise serializers.ValidationError({'CPF': 'CPF deve ser numerico'})
                
        return data

    def validate_tipo(self, tipo):
        tipo_list = ["PF", "PJ"]
        if tipo not in tipo_list:
             raise serializers.ValidationError(
                {'Tipo':"Tipo deve ser apenas PF (pessoa fisica) ou PJ (pessoa juridica)"})
        return tipo

    # def validate_nome(self, nome):
    #     if nome.isdigit():
    #         raise serializers.ValidationError({'Nome': 'Nome deve conter apenas letras'})
    #     return nome

    def validate_cod_conta(self, cod_conta):
        if not re.match(r'^([\s\d]+)$', cod_conta):
            raise serializers.ValidationError({'Cod_conta': 'Codigo da conta deve ser numerico'})
        cod_conta_list = Usuario.objects.all()
        if Usuario.objects.filter(cod_conta=cod_conta):
            raise serializers.ValidationError({'Cod_conta': 'Codigo da conta ja existente'})
        return cod_conta