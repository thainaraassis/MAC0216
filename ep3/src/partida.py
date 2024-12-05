from readchar import readkey, key
from tela import Tela
from peça import Peça
#from movimento import Movimento
from time import sleep
import random

class Partida:
    
    def __init__(self, nome_jogador, num_linhas, num_colunas):
        self.nome_jogador = nome_jogador
        self.num_linhas = int(num_linhas)
        self.num_colunas = int(num_colunas)
        self.pontuacao = 0
        self.partida_rodando = True
        self.peça_atual = Peça(0, ((self.num_colunas - 1) // 2) )
        self.matriz_jogo = self.gera_matriz_inicial()
        self.tela = Tela(self.matriz_jogo) 
        self.nova_peça = False
    
    def gera_matriz_inicial(self):

        matriz_inicial = []  

        for _ in range(self.num_linhas):  
            linha = []  
            for _ in range(self.num_colunas):  
                linha.append(" ")  
            matriz_inicial.append(linha)  

        return matriz_inicial

    def copia_matriz(self, matriz_ref):

        matriz_copia = []  

        for i in range(len(matriz_ref)):  
            linha = []  
            for j in range(len(matriz_ref[0])):  
                linha.append(matriz_ref[i][j])  

            matriz_copia.append(linha)  

        return matriz_copia
    
    def desenha_peça_na_matriz(self):

        for i in range(len(self.peça_atual.matriz_peça)):  
            for j in range(len(self.peça_atual.matriz_peça[i])):  
                caracter = self.peça_atual.matriz_peça[i][j]
                if caracter != " ":
                    x = self.peça_atual.pos_x + i  # calcula x na matriz do jogo
                    y = self.peça_atual.pos_y + j  # calcula y na matriz do jogo

                    if 0 <= x < len(self.matriz_jogo) and 0 <= y < len(self.matriz_jogo[0]):
                        self.matriz_jogo[x][y] = caracter  
                        

    def apaga_peça_na_matriz(self):

        for i in range(len(self.peça_atual.matriz_peça)):
            for j in range(len(self.peça_atual.matriz_peça[i])):
                caracter = self.peça_atual.matriz_peça[i][j]
                if caracter != " ":
                    x = self.peça_atual.pos_x + i 
                    y = self.peça_atual.pos_y + j
                    if 0 <= x < self.num_linhas and 0 <= y < self.num_colunas:
                        self.matriz_jogo[x][y] = " "  


    def captura_teclas(self):

        while True:
            tecla = readkey()

            if tecla == key.DOWN:
                self.movimento_vertical()
                break
            
            elif tecla == key.RIGHT:
                self.movimento_horizontal("direita")
                break
            
            elif tecla == key.LEFT:
                self.movimento_horizontal("esquerda")
                break
            
            elif tecla == key.PAGE_DOWN:
                self.movimento_rotaciona("esquerda")
                break
            
            elif tecla == key.PAGE_UP: 
                self.movimento_rotaciona("direita")
                break

            elif tecla == "s" or tecla == "S":
                self.para_partida()
                break
            elif tecla == "g" or tecla == "G":
                self.grava_sai_partida()
                break
            else:
                print("--------------")
                print("Tecla inválida")
                print("--------------")
                sleep(1)
                self.tela.limpa_tela()
                self.tela.exibe_matriz()
                self.tela.exibe_comandos()
                

    def atualiza_pontuaçao(self):
        """
        a cada atualização de movimento verifica cada linha se esta totalmente preenchida?
        """

    def verifica_fim_de_jogo(self, matriz_peça, pos_x_peça, pos_y_peça):
        """
        Verifica se alguma peça está no centro e no topo da matriz
        se não for possível adicionar uma nova peça sem que ela colida
        """

        if self.pode_colocar_na_posicao(matriz_peça, pos_x_peça, pos_y_peça):
            self.partida_rodando = True
        
        else:
            self.partida_rodando = False

    def jogar(self):

        while self.partida_rodando:

            self.desenha_peça_na_matriz()
            self.tela.matriz_jogo = self.copia_matriz(self.matriz_jogo)

            self.tela.exibe_matriz()
            self.tela.exibe_comandos()

            # Captura os movimentos do jogador
            self.captura_teclas()

            # Verifica se uma nova peça deve ser gerada
            if self.nova_peça:
                self.peça_atual = Peça(0, ((self.num_colunas - 1) // 2)) 
                self.nova_peça = False  
                self.verifica_fim_de_jogo(self.peça_atual.matriz_peça, self.peça_atual.pos_x, self.peça_atual.pos_y)
                #self.verifica_linhas_completas()  
                

            self.tela.limpa_tela()

        print("GAME OVER!!!!!!!")
        self.tela.exibe_comandos_game_over()
        # TRATAR

    


############################ MUDAR PRA OUTRA CLASSE ############################

    def movimento_vertical(self):
        """
        se possível move a peça para baixo e desenha na matriz do jogo
        """
        if self.pode_mover_para_baixo():
            self.apaga_peça_na_matriz()
            self.peça_atual.pos_x += 1
            self.desenha_peça_na_matriz()
        else:
            self.desenha_peça_na_matriz()
            self.nova_peça = True  


    def movimento_horizontal(self,direçao):
        """
        se possível move a peça na horizontal e desenha na matriz do jogo
        """
        if direçao == "direita" and self.pode_mover_para_direita():
            self.apaga_peça_na_matriz()
            self.peça_atual.pos_y += 1 
            self.desenha_peça_na_matriz()

        elif direçao == "esquerda" and self.pode_mover_para_esquerda():
            self.apaga_peça_na_matriz()
            self.peça_atual.pos_y -= 1  
            self.desenha_peça_na_matriz()


    def movimento_rotaciona(self,direçao):
        """
        rotaciona a peça atual 90° para a direita ou para a esquerda
        """

        self.peça_auxiliar = Peça(self.peça_atual.pos_x, self.peça_atual.pos_y)
        matriz_atual_peça = self.peça_auxiliar.matriz_peça = self.copia_matriz(self.peça_atual.matriz_peça)

        # Rotações baseadas na direção
        if direçao == "direita":
            nova_matriz_rotacionada = self.peça_auxiliar.rotacionar_direita(matriz_atual_peça)
        elif direçao == "esquerda":
            nova_matriz_rotacionada = self.peça_auxiliar.rotacionar_esquerda(matriz_atual_peça)

        self.apaga_peça_na_matriz()

        if self.pode_colocar_na_posicao(nova_matriz_rotacionada, self.peça_auxiliar.pos_x, self.peça_auxiliar.pos_y):
            # aplica a rotação na peça atual
            self.peça_atual.matriz_peça = self.copia_matriz(nova_matriz_rotacionada)
            
            self.peça_atual.pos_x = self.peça_auxiliar.pos_x
            self.peça_atual.pos_y = self.peça_auxiliar.pos_y

        self.desenha_peça_na_matriz()

    def pode_mover_para_esquerda(self):
        """
        verifica se a peça pode se mover para a esquerda
        """
        primeira_coluna_peça = 0

        for i in range(len(self.peça_atual.matriz_peça)):
            if self.peça_atual.matriz_peça[i][primeira_coluna_peça] != " ":
                x = self.peça_atual.pos_x + i
                y = self.peça_atual.pos_y + primeira_coluna_peça - 1  

                # colide com outra peça ou a grade à esquerda
                if y < 0 or self.matriz_jogo[x][y] != " ":
                    return False  
        return True

    def pode_mover_para_direita(self):
        """
        verifica se a peça pode se mover para a direita
        """
        ultima_coluna_peça = len(self.peça_atual.matriz_peça[0]) - 1

        for i in range(len(self.peça_atual.matriz_peça)):              
            if self.peça_atual.matriz_peça[i][ultima_coluna_peça] != " ":  
                x = self.peça_atual.pos_x + i  
                y = self.peça_atual.pos_y + ultima_coluna_peça + 1  

                # colide com outra peça ou a grade à direita
                if y >= self.num_colunas or self.matriz_jogo[x][y] != " ":
                    return False  

        return True  

    def pode_mover_para_baixo(self):
        """
        verifica se a peça pode se mover para baixo
        """
        for i in range(len(self.peça_atual.matriz_peça)):  
            for j in range(len(self.peça_atual.matriz_peça[0])):  
                
                if self.peça_atual.matriz_peça[i][j] != " ":  
                    proxima_linha_peça = i + 1  

                    # verifica as células da peça que estão na última linha ou
                    # as que abaixo é vazio
                    if ((proxima_linha_peça >= len(self.peça_atual.matriz_peça))
                        or (self.peça_atual.matriz_peça[proxima_linha_peça][j] == " ")):

                        # verifica a célula abaixo na matriz do jogo
                        x = self.peça_atual.pos_x + i + 1  
                        y = self.peça_atual.pos_y + j  

                        # colide com outra peça ou a grade
                        if x >= self.num_linhas or self.matriz_jogo[x][y] != " ":
                            return False

        return True  

    def pode_colocar_na_posicao(self, nova_matriz_peça, nova_pos_x, nova_pos_y):
        """
        verifica se a nova matriz da peça pode ser colocada na nova posição sem ultrapassar limites
        ou colidir com outras peças
        """
        for i in range(len(nova_matriz_peça)):
            for j in range(len(nova_matriz_peça[0])):
                if nova_matriz_peça[i][j] != " ":
                    x = nova_pos_x + i
                    y = nova_pos_y + j

                    # Verifica limites da grade
                    if x < 0 or x >= self.num_linhas or y < 0 or y >= self.num_colunas:
                        return False

                    # Verifica colisão com outra peça
                    if self.matriz_jogo[x][y] != " ":
                        return False
        return True

