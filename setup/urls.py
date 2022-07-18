
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from banco_digital.views.saldo_viewset import SaldoViewset
from banco_digital.views.transferencias_viewset import TransferenciasViewset
from banco_digital.views.usuario_viewset import UsuarioViewset
from banco_digital.views.consultar_transferencias_viewset import ConsultarEnviadasViewset, ConsultarRecebidasViewset

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewset)
router.register(r'transferencias', TransferenciasViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<int:cod_conta>/saldo/', SaldoViewset.as_view()),
    path('transferencias/<int:cod_conta>/enviadas/', ConsultarEnviadasViewset.as_view()),
    path('transferencias/<int:cod_conta>/recebidas/', ConsultarRecebidasViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
