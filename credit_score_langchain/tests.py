"""
Testes unitários para ferramentas LangChain.
"""
import unittest
from tools import calcular_score, analisar_risco

class TestLangChainTools(unittest.TestCase):
    def test_score(self):
        # 500 + 250 - 100 + 200 = 850
        self.assertEqual(calcular_score.invoke({"renda": 5000, "divida_total": 1000, "historico_pagamento": "bom"}), 850)

    def test_risco(self):
        res = analisar_risco.invoke({"score": 850})
        self.assertIn("Baixo Risco", res)

if __name__ == "__main__":
    unittest.main()
