from rest_framework import generics
from banco_digital.models.usuario import Usuario
from banco_digital.serializers.saldo_serializer import SaldoSerializer
from rest_framework.permissions import IsAuthenticated

class SaldoViewset(generics.ListAPIView):

    def get_queryset(self):
        queryset = Usuario.objects.filter(cod_conta=self.kwargs['cod_conta'])
        return queryset
    serializer_class = SaldoSerializer

    permission_classes = (IsAuthenticated,)    