import re

def validate_license_plate(plate):
    # Expressão regular para validar placas no formato "LLL-DDDD", onde L é uma letra e D é um dígito
    pattern = r'^[A-Z]{3}-\d{4}$'
    if re.match(pattern, plate):
        return "Válido"
    else:
        return "Inválido"
