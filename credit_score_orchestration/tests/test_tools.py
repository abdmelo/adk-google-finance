"""
Testes unitários para as ferramentas do sistema de orquestração.
"""
import sys
import os
# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import calcular_score_detalhado, calcular_oferta_emprestimo

def test_calcular_score_detalhado_bom():
    resultado = calcular_score_detalhado(5000, 1000, 'bom')
    # Base 500 + (5000*0.05=250) - (1000*0.1=100) + 200 = 850
    assert resultado['score'] == 850
    assert resultado['detalhes']['fator_historico'] == 200

def test_calcular_score_detalhado_ruim():
    resultado = calcular_score_detalhado(5000, 1000, 'ruim')
    # Base 500 + 250 - 100 - 200 = 450
    assert resultado['score'] == 450

def test_oferta_emprestimo_aprovado():
    # Score alto, parcela cabe na renda
    # Renda 10000 -> limite 3000
    # Empréstimo 10000 -> juros baixos -> parcela ~900
    resultado = calcular_oferta_emprestimo(800, 10000, 10000)
    assert resultado['aprovado'] is True
    assert resultado['valor_aprovado'] == 10000

def test_oferta_emprestimo_reprovado_score():
    resultado = calcular_oferta_emprestimo(300, 10000, 10000)
    assert resultado['aprovado'] is False
    assert "Score insuficiente" in resultado['motivo']

def test_oferta_emprestimo_reprovado_renda():
    # Renda baixa, empréstimo alto
    # Renda 1000 -> limite 300
    # Empréstimo 10000 -> parcela > 300
    resultado = calcular_oferta_emprestimo(700, 1000, 10000)
    assert resultado['aprovado'] is False
    assert "excede 30% da renda" in resultado['motivo']

if __name__ == "__main__":
    # Execução manual simples se pytest não estiver instalado
    try:
        test_calcular_score_detalhado_bom()
        test_calcular_score_detalhado_ruim()
        test_oferta_emprestimo_aprovado()
        test_oferta_emprestimo_reprovado_score()
        test_oferta_emprestimo_reprovado_renda()
        print("Todos os testes passaram com sucesso!")
    except AssertionError as e:
        print(f"Falha no teste: {e}")
    except Exception as e:
        print(f"Erro: {e}")
