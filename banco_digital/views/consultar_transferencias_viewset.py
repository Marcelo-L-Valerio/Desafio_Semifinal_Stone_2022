from rest_framework import generics, filters
from banco_digital.models.transferencias import Transferencias
from banco_digital.serializers.consultar_transferencias_serializer import ConsultarTransferenciaSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ConsultarEnviadasViewset(generics.ListAPIView):

    def get_queryset(self):
        queryset = Transferencias.objects.filter(conta_origem=self.kwargs['cod_conta'])
        return queryset

    serializer_class = ConsultarTransferenciaSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['data_transferencia', 'conta_destino']
    ordering_fields = ['data_transferencia']
    
class ConsultarRecebidasViewset(generics.ListAPIView):

    def get_queryset(self):
        queryset = Transferencias.objects.filter(conta_destino=self.kwargs['cod_conta'])
        return queryset

    serializer_class = ConsultarTransferenciaSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['data_transferencia', 'conta_origem']
    ordering_fields = ['data_transferencia']