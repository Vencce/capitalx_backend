from rest_framework import viewsets
from .models import Carta, Administradora
from .serializers import CartaSerializer, AdministradoraSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AdministradoraViewSet(viewsets.ModelViewSet):
    queryset = Administradora.objects.all()
    serializer_class = AdministradoraSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CartaViewSet(viewsets.ModelViewSet):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]