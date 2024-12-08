import pytest
from partida import Partida


@pytest.fixture()
def partida_teste():
    partida = Partida("Teste", 10, 10)
    partida.peça_atual.matriz_peça = partida.peça_atual.gera_peça("T")
    # desenha peças já na matriz?
    return partida


class Test_Partida():
    def test_desenha_na_matriz_peça_posiçao_inicial(self, partida_teste):
        """
        testa se a peça gerada vai ser colocada na  posição  inicial correta
        """
        partida_teste.desenha_peça_na_matriz()

        matriz_jogo_esperada = [
            [ " ", " ", " ", " ", '+', '+', '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", '+', " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
        ]

        assert partida_teste.matriz_jogo == matriz_jogo_esperada

    def test_desenha_na_matriz_peça_posiçao_qualquer(self, partida_teste):

        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 5
        partida_teste.desenha_peça_na_matriz()

        matriz_jogo_esperada = [
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", '+', '+', '+', " ", " "],
            [ " ", " ", " ", " ", " ", " ", '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
        ]

        assert partida_teste.matriz_jogo == matriz_jogo_esperada

    def test_apaga_na_matriz(self, partida_teste):

        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 5
        partida_teste.desenha_peça_na_matriz()
        partida_teste.apaga_peça_na_matriz()

        matriz_jogo_esperada = [
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
        ]

        assert partida_teste.matriz_jogo == matriz_jogo_esperada

    def test_peça_move_na_vertical(self, partida_teste):

        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 5
        partida_teste.desenha_peça_na_matriz()
        partida_teste.movimento_vertical()

        matriz_jogo_esperada = [
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", '+', '+', '+', " ", " "],
            [ " ", " ", " ", " ", " ", " ", '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
        ]

        assert partida_teste.matriz_jogo == matriz_jogo_esperada

    def test_peça_nao_move_na_vertical(self, partida_teste):

        # inclui a peça mais abaixo
        partida_teste.peça_atual.pos_x = 7
        partida_teste.peça_atual.pos_y = 5
        partida_teste.desenha_peça_na_matriz()

        # inclui a peça mais acima
        partida_teste.peça_atual.gera_peça("T")
        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 5
        partida_teste.desenha_peça_na_matriz()

        # tenta mover a peça mais acima para baixo 
        # o movimento não é realizado e peça permanece imóvel
        partida_teste.movimento_vertical()

        matriz_jogo_esperada = [
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", '+', '+', '+', " ", " "],
            [ " ", " ", " ", " ", " ", " ", '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", '+', '+', '+', " ", " "],
            [ " ", " ", " ", " ", " ", " ", '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
        ]

        assert partida_teste.matriz_jogo == matriz_jogo_esperada

