import unittest
from logical_operations import logical_and

# RF04 - Entrada: P = Número binário, Número binário | Saída: (0;1) // Algoritmo de uma operação lógica AND.

class TestLogicalOperations(unittest.TestCase):
    
    def test_logical_and(self):
        # Caso de teste para realizar a operação lógica AND entre dois números binários
        bin1 = "1010"
        bin2 = "1100"
        expected_result = "1000"
        result = logical_and(bin1, bin2)
        self.assertEqual(result, expected_result, f"O resultado da operação lógica AND entre {bin1} e {bin2} deveria ser {expected_result}.")

    def test_logical_and_all_zeros(self):
        # Caso de teste para realizar a operação lógica AND entre dois números binários que são todos zeros
        bin1 = "0000"
        bin2 = "0000"
        expected_result = "0000"
        result = logical_and(bin1, bin2)
        self.assertEqual(result, expected_result, f"O resultado da operação lógica AND entre {bin1} e {bin2} deveria ser {expected_result}.")

    def test_logical_and_all_ones(self):
        # Caso de teste para realizar a operação lógica AND entre dois números binários que são todos uns
        bin1 = "1111"
        bin2 = "1111"
        expected_result = "1111"
        result = logical_and(bin1, bin2)
        self.assertEqual(result, expected_result, f"O resultado da operação lógica AND entre {bin1} e {bin2} deveria ser {expected_result}.")

if __name__ == '__main__':
    unittest.main()
