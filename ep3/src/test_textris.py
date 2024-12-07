import pytest
from partida import Partida
from peça import Peça
from movimento import Movimento

matriz_jogo_NAO_DIREITA_BAIXO_esquerda = [
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [ " ", " ", " ", '+', '+', '+', " ", " ", " ", " "],
            [ " ", " ", " ", " ", '+', '+', '+', '+', " ", " "],
            [ " ", " ", " ", " ", " ", " ", '+', " ", " ", " "],
            [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            
]

@pytest.fixture()
def partida_teste():
    partida = Partida("Teste", 10, 10)
    partida.peça_atual.matriz_peça = partida.peça_atual.gera_peça("T")
    # desenha peças já na matriz?
    return partida

@pytest.fixture()
def peça_teste():
    peça = Peça(5,5)
    peça.matriz_peça = peça.gera_peça("T")
    return peça

@pytest.fixture()
def dic_peças():
    dicionario_peças = {
        "I" :   [   ['&'],
                    ['&'],
                    ['&'],
                    ['&']
                ],
        
        "J" :   [   [" ", '$'],
                    [" ", '$'],
                    [" ", '$'],
                    ['$', '$']
                ],

        "L" :   [   ['*', " "],
                    ['*', " "],
                    ['*', " "],
                    ['*', '*']

                ],

        "O" :   [   ['@', '@'],
                    ['@', '@']

                ],
        
        "S" :   [   [' ', '%', '%'],
                    ['%', '%', ' ']

                ],

        "T" :   [   ['+', '+', '+'],
                    [' ', '+', ' ']

                ],

        "Z" :   [   ['#', '#', ' '],
                    [' ', '#', '#']

                ] 

    }

    return dicionario_peças


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


class Test_Peça():

    def test_gera_peça_aleatoria(self, peça_teste, dic_peças):
        # No jogo é gerado aleatoriamente, contudo para fins de testes
        # geraremos uma peça específica

        foi_gerada = False
        #foi_gerada =  peça_teste.matriz_jogo in dic_peças
        for alguma_peça in dic_peças:
            if peça_teste.matriz_peça == alguma_peça:
                foi_gerada = True
                break
            
        assert foi_gerada == True
    
    def test_rotacionar_pra_direita(self, peça_teste):

        nova_peça_teste = peça_teste.rotacionar_direita(peça_teste.matriz_peça)

        peça_esperada = [
            [" ", '+'],
            ['+', '+'],
            [" ", '+']
        ]

        assert nova_peça_teste == peça_esperada

    def test_rotacionar_pra_esquerda(self, peça_teste):

        nova_peça_teste = peça_teste.rotacionar_esquerda(peça_teste.matriz_peça)

        peça_esperada = [
            ['+', " "],
            ['+', '+'],
            ['+', " "]
        ]

        assert nova_peça_teste == peça_esperada

class Test_Movimento():
    



    def test_pode_mover_peça_para_baixo(self, partida_teste):
        
        partida_teste.desenha_peça_na_matriz()

        pode_mover_baixo = Movimento.pode_mover_para_baixo(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        assert pode_mover_baixo == True

    def test_nao_pode_mover_peça_para_baixo(self, partida_teste):

        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 7
        partida_teste.desenha_peça_na_matriz()

        partida_teste.peça_atual.gera_peça("T")
        partida_teste.peça_atual.pos_x = 3
        partida_teste.peça_atual.pos_y = 6
        partida_teste.desenha_peça_na_matriz()

        nao_pode_mover_baixo = Movimento.pode_mover_para_baixo(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        #assert nao_pode_mover_baixo == False
        assert partida_teste.matriz_jogo == matriz_jogo_NAO_DIREITA_BAIXO_esquerda
    def test_pode_mover_peça_para_esquerda(self, partida_teste):
    
        partida_teste.desenha_peça_na_matriz()

        pode_mover_esquerda = Movimento.pode_mover_para_esquerda(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        assert pode_mover_esquerda == True

    def test_nao_pode_mover_peça_para_esquerda(self, partida_teste):

        partida_teste.peça_atual.pos_x = 3 
        partida_teste.peça_atual.pos_y = 6 
        partida_teste.desenha_peça_na_matriz()

        partida_teste.peça_atual.gera_peça("T")
        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 7
        partida_teste.desenha_peça_na_matriz()

        nao_pode_mover_esquerda = Movimento.pode_mover_para_esquerda(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        #assert nao_pode_mover_esquerda == False
        assert partida_teste.matriz_jogo == matriz_jogo_NAO_DIREITA_BAIXO_esquerda

    def test_pode_mover_peça_para_direita(self, partida_teste):
    
        partida_teste.desenha_peça_na_matriz()

        pode_mover_direita = Movimento.pode_mover_para_direita(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        assert pode_mover_direita == True


    def test_nao_pode_mover_peça_para_direita(self, partida_teste):

        partida_teste.peça_atual.pos_x = 5
        partida_teste.peça_atual.pos_y = 7
        partida_teste.desenha_peça_na_matriz()

        partida_teste.peça_atual.gera_peça("T")
        partida_teste.peça_atual.pos_x = 3
        partida_teste.peça_atual.pos_y = 6
        partida_teste.desenha_peça_na_matriz()

        nao_pode_mover_direita = Movimento.pode_mover_para_direita(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        #assert nao_pode_mover_direita == False
        assert partida_teste.matriz_jogo == matriz_jogo_NAO_DIREITA_BAIXO_esquerda

    def test_pode_colocar_peça(self, partida_teste):

        partida_teste.desenha_peça_na_matriz()

        pode_colocar_peça = Movimento.pode_colocar_na_posicao(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)
        
        assert pode_colocar_peça == True

    def test_nao_pode_colocar_peça(self, partida_teste):
      
        partida_teste.desenha_peça_na_matriz()
        partida_teste.peça_atual.gera_peça("T")

        nao_pode_colocar_peça = Movimento.pode_colocar_na_posicao(partida_teste.peça_atual.matriz_peça, partida_teste.matriz_jogo, partida_teste.peça_atual.pos_x, partida_teste.peça_atual.pos_y)

        assert nao_pode_colocar_peça == False