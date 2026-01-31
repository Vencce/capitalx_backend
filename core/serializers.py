from rest_framework import serializers
from .models import Carta, Administradora

class AdministradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradora
        fields = '__all__'

class CartaSerializer(serializers.ModelSerializer):
    administradora_detalhes = AdministradoraSerializer(source='administradora', read_only=True)
    
    administradora = serializers.PrimaryKeyRelatedField(queryset=Administradora.objects.all())

    class Meta:
        model = Carta
        fields = '__all__'