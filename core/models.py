from django.db import models
import uuid

class Administradora(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos_bancos/')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Administradora"
        verbose_name_plural = "Administradoras"

class Carta(models.Model):
    TIPO_CHOICES = [
        ('IMOVEL', 'Imóvel'),
        ('AUTOMOVEL', 'Automóvel'),
    ]

    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('RESERVADO', 'Reservado'),
        ('VENDIDO', 'Vendido'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    administradora = models.ForeignKey(Administradora, on_delete=models.CASCADE, related_name='cartas')
    
    # Valores Financeiros Principais
    valor_credito = models.DecimalField(max_digits=12, decimal_places=2)
    valor_entrada = models.DecimalField(max_digits=12, decimal_places=2)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    numero_parcelas = models.IntegerField()
    
    # Detalhes Opcionais (Só aparecem se preenchidos)
    saldo_devedor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="Saldo Devedor")
    seguro_vida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Seguro de Vida")
    
    # Especificações
    vencimento = models.DateField(null=True, blank=True, verbose_name="Próximo Vencimento / Validade")
    
    # Agora aceita texto (Ex: "Grátis", "1 Salário")
    taxa_transferencia = models.CharField(max_length=100, default="Grátis", verbose_name="Taxa de Transferência")
    
    tipo_contemplacao = models.CharField(max_length=50, default="Sorteio", help_text="Ex: Sorteio, Lance")
    observacoes = models.TextField(null=True, blank=True, verbose_name="Observações Gerais")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')
    
    # (Campo Imagem REMOVIDO)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.administradora.nome}"

    class Meta:
        ordering = ['-criado_em']
        verbose_name = "Carta Contemplada"
        verbose_name_plural = "Cartas Contempladas"

class Configuracao(models.Model):
    """
    Modelo Singleton para guardar configurações gerais do site
    como número de WhatsApp, Links de Redes Sociais, etc.
    """
    whatsapp = models.CharField(max_length=20, default="5547999999999", help_text="Apenas números (ex: 5547999999999)")
    email_contato = models.EmailField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Configurações Gerais do Site"

    class Meta:
        verbose_name = "Configuração Geral"
        verbose_name_plural = "Configurações Gerais"