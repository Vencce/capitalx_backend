import requests
from decimal import Decimal
from .models import Carta, Administradora

def executar_sincronizacao():
    url = "https://fragaebitelloconsorcios.com.br/api/json/contemplados"
    
    try:
        response = requests.get(url, timeout=20)
        if response.status_code != 200:
            return None
            
        dados_api = response.json()
        novas = 0
        atualizadas = 0

        for item in dados_api:
            # 1. Busca ou Cria a Administradora usando a imagem da API
            admin, _ = Administradora.objects.update_or_create(
                nome=item['administradora'].strip(),
                defaults={
                    'logo_url_externa': item.get('administradora_img')
                }
            )

            # 2. Mapeia Categoria (API: Veículo/Imóvel -> Seu Model: AUTOMOVEL/IMOVEL)
            tipo_map = {'Veículo': 'AUTOMOVEL', 'Imóvel': 'IMOVEL'}
            tipo_final = tipo_map.get(item['categoria'], 'IMOVEL')

            # 3. Mapeia Status
            status_final = 'RESERVADO' if item.get('reserva') == 'Reservado' else 'DISPONIVEL'

            # 4. Salva no Banco
            obj, created = Carta.objects.update_or_create(
                codigo=f"FB-{item['id']}", # Garante que não duplique
                defaults={
                    'tipo': tipo_final,
                    'origem': 'PARCEIRO',
                    'administradora': admin,
                    'valor_credito': Decimal(str(item['valor_credito'])),
                    'valor_entrada': Decimal(str(item['entrada'])),
                    'valor_parcela': Decimal(str(item['valor_parcela'])),
                    'numero_parcelas': int(item['parcelas']),
                    'status': status_final,
                    'observacoes': f"ID Parceiro: {item['id']}"
                }
            )

            if created: novas += 1
            else: atualizadas += 1
                
        return {"novas": novas, "atualizadas": atualizadas}
        
    except Exception as e:
        print(f"Erro na sincronização: {e}")
        return None