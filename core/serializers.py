from rest_framework import serializers
from .models import Administradora, Carta, Configuracao

class AdministradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradora
        fields = ['id', 'nome', 'logo', 'logo_url_externa']

class CartaSerializer(serializers.ModelSerializer):
    administradora_detalhes = AdministradoraSerializer(source='administradora', read_only=True)

    class Meta:
        model = Carta
        fields = [
            'id', 'codigo', 'tipo', 'valor_credito', 'valor_entrada', 
            'valor_parcela', 'numero_parcelas', 'vencimento', 
            'taxa_transferencia', 'tipo_contemplacao', 'saldo_devedor', 
            'seguro_vida', 'observacoes', 'status', 'administradora',
            'administradora_detalhes'
        ]

class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'