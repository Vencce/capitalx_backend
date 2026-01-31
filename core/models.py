from django.db import models
import uuid

class Administradora(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos_bancos/', null=True, blank=True)

    def __str__(self):
        return self.nome

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
    
    # Agora vinculamos ao modelo Administradora
    administradora = models.ForeignKey(Administradora, on_delete=models.CASCADE, related_name='cartas')
    
    valor_credito = models.DecimalField(max_digits=12, decimal_places=2)
    valor_entrada = models.DecimalField(max_digits=12, decimal_places=2)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    numero_parcelas = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')
    
    imagem = models.ImageField(upload_to='cartas/', null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.administradora.nome}"

    class Meta:
        ordering = ['-criado_em']