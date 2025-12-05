"""
Testes unitários para o projeto simples de Credit Score.
"""
import unittest
from tools import calcular_score, analisar_risco

class TestCreditScoreSimple(unittest.TestCase):
    
    def test_calcular_score_basico(self):
        # Renda 5000 (+250), Dívida 1000 (-100), Bom (+200) -> Base 500 + 350 = 850
        score = calcular_score(5000, 1000, 'bom')
        self.assertEqual(score, 850)

    def test_analisar_risco_baixo(self):
        resultado = analisar_risco(850)
        self.assertEqual(resultado['categoria'], "Baixo Risco")

    def test_analisar_risco_alto(self):
        resultado = analisar_risco(300)
        self.assertEqual(resultado['categoria'], "Alto Risco")

if __name__ == '__main__':
    unittest.main()
