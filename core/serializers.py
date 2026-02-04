from rest_framework import serializers
from .models import Administradora, Carta, Configuracao

class AdministradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradora
        fields = '__all__'

class CartaSerializer(serializers.ModelSerializer):
    administradora_nome = serializers.ReadOnlyField(source='administradora.nome')
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Carta
        fields = '__all__'

class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'