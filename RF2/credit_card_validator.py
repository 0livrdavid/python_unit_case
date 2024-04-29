import requests

def validate_credit_card(card_number, card_holder, expiration_date, security_code):
    # Algoritmo de validação do cartão de crédito (pode ser uma implementação mais detalhada)
    if len(card_number) != 16:
        return "Inválido", "Compra negada"
    
    # Simulação de comunicação com a operadora via API segura (usando a API ReqRes.in)
    api_url = "https://reqres.in/api/validate_payment"
    payload = {
        "card_number": card_number,
        "card_holder": card_holder,
        "expiration_date": expiration_date,
        "security_code": security_code
    }
    
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            if result.get("valid", False):
                return "Válido", "Compra autorizada"
            else:
                return "Válido", "Compra negada"
        else:
            return "Inválido", "Erro na comunicação com a operadora"
    except Exception as e:
        return "Inválido", "Compra negada"
