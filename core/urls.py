from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartaViewSet, AdministradoraViewSet

router = DefaultRouter()
router.register(r'cartas', CartaViewSet)
router.register(r'administradoras', AdministradoraViewSet) # Nova rota

urlpatterns = [
    path('', include(router.urls)),
]