import random

class Peça:

    def __init__(self, posiçao_x, posiçao_y):
        self.pos_x = posiçao_x
        self.pos_y = posiçao_y
        self.matriz_peça = self.gera_peça() 

    def gera_peça(self):
        """
        gera uma peça aleatória e retorna a matriz da peça 
        """
        nomes_peças = ["I", "J", "L", "O", "S", "T", "Z"]
        nome_aleatorio = nomes_peças[random.randint(0, len(nomes_peças)-1)]

        return self.peças_do_textris(nome_aleatorio)
    
    def rotacionar_direita(self, peça):
        """
        rotaciona a matriz da peça 90° para a direita (sentido horário).
        """
        linhas = len(peça)
        colunas = len(peça[0])

        nova_matriz_peça = self.devolve_matriz_vazia(colunas, linhas)

        for i in range(linhas):
            for j in range(colunas):
                nova_matriz_peça[j][linhas - i - 1] = peça[i][j]  

        return nova_matriz_peça
    
    def rotacionar_esquerda(self, peça):
        """
        rotaciona a matriz da peça 90° para a esquerda (sentido anti-horário).
        """
        linhas = len(peça)
        colunas = len(peça[0])

        nova_matriz_peça = self.devolve_matriz_vazia(colunas, linhas)

        for i in range(linhas):
            for j in range(colunas):
                nova_matriz_peça[colunas - j - 1][i] = peça[i][j]  

        return nova_matriz_peça

    def peças_do_textris(self, nome_peça):
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

        return dicionario_peças.get(nome_peça)
    
    def devolve_matriz_vazia(self, linhas, colunas):

        matriz_inicial = []  

        for _ in range(linhas):  
            linha = []  
            for _ in range(colunas):  
                linha.append(" ")  
            matriz_inicial.append(linha)  

        return matriz_inicial