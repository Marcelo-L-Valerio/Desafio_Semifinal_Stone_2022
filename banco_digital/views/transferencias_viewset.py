
from rest_framework import viewsets, filters
from banco_digital.models.transferencias import Transferencias
from banco_digital.serializers.transferencias_serializer import TransferenciasSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class TransferenciasViewset(viewsets.ModelViewSet):

    queryset = Transferencias.objects.all()
    serializer_class = TransferenciasSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['data_transferencia', 'conta_origem', 'conta_destino']
    ordering_fields = ['data_transferencia']
