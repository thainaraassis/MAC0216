import pytest
from jogador import Jogador

def test_criar_jogador():
    
    jogador = Jogador("Kelly")
    assert jogador.nome == "Kelly"
    assert jogador.pontuacao == 0

    jogador = Jogador("Henrique", 18)
    assert jogador.nome == "Henrique"
    assert jogador.pontuacao == 18

def test_atualizar_pontuacao():
    
    jogador = Jogador("Livia")
    jogador.atualizar_pontuacao(7)
    assert jogador.pontuacao == 7  

    jogador = Jogador("Julia", 11)
    jogador.atualizar_pontuacao(3)
    assert jogador.pontuacao == 14

    

