from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdministradoraViewSet, CartaViewSet, CustomLoginView, ConfiguracaoView, ExportarExcelView, ExportarPDFView, SincronizarCartasView

router = DefaultRouter()
router.register(r'administradoras', AdministradoraViewSet)
router.register(r'cartas', CartaViewSet)

urlpatterns = [
    path('cartas/sincronizar/', SincronizarCartasView.as_view(), name='sincronizar-cartas'),
    path('', include(router.urls)),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('configuracoes/', ConfiguracaoView.as_view(), name='configuracoes'),
    path('exportar/excel/', ExportarExcelView.as_view(), name='export-excel'),
    path('exportar/pdf/', ExportarPDFView.as_view(), name='export-pdf'),
]