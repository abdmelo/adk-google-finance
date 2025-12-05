"""
Testes unitários para ferramentas CrewAI.
"""
import unittest
from tools import CalcularScoreTool
 
class TestCrewAITools(unittest.TestCase):
    def test_score(self):
        # Instancia a ferramenta
        tool = CalcularScoreTool()
        # Simulação de chamada direta
        res = tool._run(renda=5000, divida_total=1000, historico_pagamento="bom")
        self.assertEqual(res, 850)

if __name__ == "__main__":
    unittest.main()
