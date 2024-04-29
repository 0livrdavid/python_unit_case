import unittest
from license_plate_validator import validate_license_plate

# RF05 - Entrada: P = Placa de um veículo | Saída: (“Valido”; “Inválido”) // Algoritmo validador de placas.

class TestLicensePlateValidator(unittest.TestCase):
    
    def test_valid_license_plate(self):
        # Caso de teste para uma placa válida
        plate = "ABC-1234"
        expected_result = "Válido"
        result = validate_license_plate(plate)
        self.assertEqual(result, expected_result, f"A placa {plate} deveria ser válida.")

    def test_invalid_license_plate(self):
        # Caso de teste para uma placa inválida
        plate = "1234-ABC"  # Formato incorreto
        expected_result = "Inválido"
        result = validate_license_plate(plate)
        self.assertEqual(result, expected_result, f"A placa {plate} deveria ser inválida.")

    def test_invalid_license_plate_characters(self):
        # Caso de teste para uma placa com caracteres inválidos
        plate = "AB!-1234"  # Caracteres especiais não permitidos
        expected_result = "Inválido"
        result = validate_license_plate(plate)
        self.assertEqual(result, expected_result, f"A placa {plate} deveria ser inválida devido a caracteres inválidos.")

if __name__ == '__main__':
    unittest.main()
