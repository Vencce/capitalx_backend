from django.contrib import admin
from .models import Carta, Administradora, Configuracao

@admin.register(Administradora)
class AdministradoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'administradora', 'valor_credito', 'vencimento', 'status')
    list_filter = ('tipo', 'status', 'administradora', 'vencimento')
    search_fields = ('codigo', 'administradora__nome', 'observacoes')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'tipo', 'administradora', 'status')
        }),
        ('Valores Financeiros', {
            'fields': ('valor_credito', 'valor_entrada', 'valor_parcela', 'numero_parcelas')
        }),
        ('Saldos e Seguros (Opcionais)', {
            'fields': ('saldo_devedor', 'seguro_vida'),
            'description': 'Preencha se houver valores específicos. Caso contrário, deixe em branco.'
        }),
        ('Especificações Técnicas', {
            'fields': ('vencimento', 'taxa_transferencia', 'tipo_contemplacao', 'observacoes')
        }),
    )

@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'email_contato', 'atualizado_em')
    
    # Impede adicionar mais de uma configuração pelo Django Admin padrão
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True