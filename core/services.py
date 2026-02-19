import requests
from decimal import Decimal
from .models import Carta, Administradora

def executar_sincronizacao():
    url = "https://fragaebitelloconsorcios.com.br/api/json/contemplados"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return None
            
        dados_api = response.json()
        novas = 0
        atualizadas = 0

        for item in dados_api:
            # 1. Trata Administradora e a Logo da API
            admin, _ = Administradora.objects.update_or_create(
                nome=item['administradora'].strip(),
                defaults={
                    'logo_url_externa': item['administradora_img']
                }
            )

            # 2. Converte Categoria
            tipo_map = {'Veículo': 'AUTOMOVEL', 'Imóvel': 'IMOVEL'}
            tipo_final = tipo_map.get(item['categoria'], 'IMOVEL')

            # 3. Salva marcando como ORIGEM = PARCEIRO
            obj, created = Carta.objects.update_or_create(
                codigo=f"FB-{item['id']}",
                defaults={
                    'tipo': tipo_final,
                    'origem': 'PARCEIRO',  # <--- SEPARAÇÃO AQUI
                    'administradora': admin,
                    'valor_credito': Decimal(str(item['valor_credito'])),
                    'valor_entrada': Decimal(str(item['entrada'])),
                    'valor_parcela': Decimal(str(item['valor_parcela'])),
                    'numero_parcelas': int(item['parcelas']),
                    'status': 'DISPONIVEL' if item.get('reserva') == 'Disponivel' else 'RESERVADO',
                    'observacoes': f"Importado automaticamente (ID: {item['id']})"
                }
            )

            if created: novas += 1
            else: atualizadas += 1
                
        return {"novas": novas, "atualizadas": atualizadas}
        
    except Exception as e:
        print(f"Erro: {e}")
        return None