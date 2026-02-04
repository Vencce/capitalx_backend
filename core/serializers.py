from rest_framework import serializers
from .models import Administradora, Carta, Configuracao

class AdministradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradora
        fields = '__all__'

class CartaSerializer(serializers.ModelSerializer):
    # Campo aninhado para leitura (traz o nome e logo do banco junto com a carta)
    administradora_detalhes = AdministradoraSerializer(source='administradora', read_only=True)

    class Meta:
        model = Carta
        fields = '__all__'
        extra_kwargs = {
            'administradora': {'write_only': True} # O ID é usado apenas na escrita
        }

# Esta é a classe que estava faltando e causou o erro:
class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'