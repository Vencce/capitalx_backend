from django.contrib import admin
from .models import Carta

@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'administradora', 'valor_credito', 'status')
    list_filter = ('tipo', 'status', 'administradora')
    search_fields = ('codigo', 'administradora')