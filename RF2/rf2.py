import unittest
from credit_card_validator import validate_credit_card

# RF02 - Entrada: P = Número de um Cartão de Crédito; Nome do Titular; Validade; Código de Segurança | 
# Saída: {(“Valido”; “Inválido”),(“Compra autorizada”;”Compra negada”)}. // i-Algoritmo validador de Cartão de Crédito; 
# ii -comunica via API segura com operadora e verifica se a compra pode ou não ser finalizada.

class TestCreditCardValidator(unittest.TestCase):
    
    def test_valid_credit_card(self):
        # Caso de teste para um cartão de crédito válido
        card_number = "4111111111111111"  # Um número de cartão de teste aceito pela API ReqRes.in
        card_holder = "John Doe"
        expiration_date = "12/25"
        security_code = "123"
        status, message = validate_credit_card(card_number, card_holder, expiration_date, security_code)
        self.assertEqual(status, "Válido", f"O cartão de crédito {card_number} deveria ser válido.")
        self.assertEqual(message, "Compra autorizada", f"A compra com o cartão de crédito {card_number} deveria ser autorizada.")

    def test_invalid_credit_card(self):
        # Caso de teste para um cartão de crédito inválido
        card_number = "1234567890123456"  # Um número de cartão inválido
        card_holder = "Jane Doe"
        expiration_date = "12/25"
        security_code = "123"
        status, message = validate_credit_card(card_number, card_holder, expiration_date, security_code)
        self.assertEqual(status, "Inválido", f"O cartão de crédito {card_number} deveria ser inválido.")
        self.assertEqual(message, "Compra negada", f"A compra com o cartão de crédito {card_number} deveria ser negada.")

    def test_invalid_card_number_length(self):
        # Caso de teste para um número de cartão com comprimento inválido
        card_number = "1234567890"  # Número de cartão com comprimento inválido
        card_holder = "Jose Silva"
        expiration_date = "12/25"
        security_code = "123"
        status, message = validate_credit_card(card_number, card_holder, expiration_date, security_code)
        self.assertEqual(status, "Inválido", f"O cartão de crédito {card_number} deveria ser inválido devido ao comprimento.")
        self.assertEqual(message, "Compra negada", f"A compra com o cartão de crédito {card_number} deveria ser negada devido ao comprimento.")

if __name__ == '__main__':
    unittest.main()
