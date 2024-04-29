import unittest
from currency_converter import convert_currency

# RF03 - Entrada: P = Valor em R$ | Saída: (Valor em $). // Algoritmo conversor de moedas em tem real.

class TestCurrencyConverter(unittest.TestCase):
    
    def test_convert_currency(self):
        # Caso de teste para converter um valor em R$ para $
        amount = 100  # R$100,00
        expected_result = 100 / 5.12  # Valor esperado em $
        result = convert_currency(amount)
        self.assertAlmostEqual(result, expected_result, places=2, msg=f"O valor convertido deveria ser aproximadamente {expected_result}, mas foi {result}.")

    def test_convert_zero_currency(self):
        # Caso de teste para converter zero reais para dólares
        amount = 0  # R$0,00
        expected_result = 0  # Valor esperado em $
        result = convert_currency(amount)
        self.assertAlmostEqual(result, expected_result, places=2, msg=f"O valor convertido deveria ser aproximadamente {expected_result}, mas foi {result}.")

    def test_convert_large_currency(self):
        # Caso de teste para converter um valor grande em R$ para dólares
        amount = 1000000  # R$1.000.000,00
        expected_result = 1000000 / 5.12  # Valor esperado em $
        result = convert_currency(amount)
        self.assertAlmostEqual(result, expected_result, places=2, msg=f"O valor convertido deveria ser aproximadamente {expected_result}, mas foi {result}.")

if __name__ == '__main__':
    unittest.main()
