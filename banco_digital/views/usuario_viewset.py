from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from banco_digital.models.usuario import Usuario
from banco_digital.serializers.usuario_serializer import UsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewset(viewsets.ModelViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['nome', 'cpf', 'cnpj']
    ordering_fields = ['nome']