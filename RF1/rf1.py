import unittest
from cpf_validator import validate_cpf

# RF01 - Entrada: P = Número de um CPF | Saída: (‘False’; ‘True’). // Algoritmo validador de CPF.

class TestCPFValidator(unittest.TestCase):
    def test_valid_cpf(self):
        # Caso de teste para um CPF válido
        cpf = "123.456.789-09"
        self.assertTrue(validate_cpf(cpf), f"O CPF {cpf} deveria ser válido.")

    def test_invalid_cpf(self):
        # Caso de teste para um CPF inválido
        cpf = "123.456.789-00"
        self.assertFalse(validate_cpf(cpf), f"O CPF {cpf} deveria ser inválido.")

    def test_invalid_format(self):
        # Caso de teste para um CPF com formato inválido
        cpf = "12345678900"  # formato sem pontos e traço
        self.assertFalse(validate_cpf(cpf), f"O formato do CPF {cpf} é inválido.")

if __name__ == '__main__':
    unittest.main()
