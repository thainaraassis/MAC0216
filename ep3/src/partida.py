from readchar import readkey, key
from tela import Tela
from peça import Peça
from movimento import Movimento
from matriz import Matriz
from time import sleep
from jogador import Jogador
from ranking import Ranking
from datetime import datetime
import pickle

class Partida:
    
    def __init__(self, nome_jogador, num_linhas, num_colunas):
        self.jogador = Jogador(nome_jogador)
        self.num_linhas = int(num_linhas)
        self.num_colunas = int(num_colunas)
        self.pontuacao = 0
        self.partida_rodando = True
        self.peça_atual = Peça(0, ((self.num_colunas - 1) // 2) )
        self.matriz_jogo = Matriz.devolve_matriz_vazia(self.num_linhas,self.num_colunas)
        self.tela = Tela(self.matriz_jogo) 
        self.nova_peça = False
        self.exibe_salvamento = False
    
    def jogar(self):

        while self.partida_rodando:

            self.desenha_peça_na_matriz()
            self.tela.matriz_jogo = Matriz.copia_matriz(self.matriz_jogo)

            self.tela.exibe_matriz()
            self.tela.exibe_comandos(self.pontuacao)

            # Captura os movimentos do jogador
            self.captura_teclas()

            # Verifica se uma nova peça deve ser gerada
            if self.nova_peça:
                self.peça_atual = Peça(0, ((self.num_colunas - 1) // 2)) 
                self.nova_peça = False  
                self.verifica_fim_de_jogo(self.peça_atual.matriz_peça, self.peça_atual.pos_x, self.peça_atual.pos_y)
                self.atualiza_pontuaçao()  
                

            self.tela.limpa_tela()

        if self.exibe_salvamento:
            self.tela.exibe_comandos_salvamento_partida()
        else:    
            Ranking.ranks.append(self.jogador)
            self.tela.exibe_comandos_game_over(self.pontuacao)
 
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
                self.tela.exibe_comandos(self.pontuacao)
                
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


    def atualiza_pontuaçao(self):
        """
        a cada atualização de movimento verifica cada linha se esta totalmente preenchida?
        """

        linhas_remover = [] # vai guardar os índices das linhas para remover

        # agora, vamos percorrer todos elementos da matriz
        # se temos que uma linha todos elementos NÃO são " ", que dizer que a linha está preenchida
        # e podemos removê-las
        for i in range(len(self.matriz_jogo)):  
            linha_preenchida = True  

            for c in self.matriz_jogo[i]:  
                if c == " ":  
                    linha_preenchida = False
                    break  

            if linha_preenchida:  
                linhas_remover.append(i)

        # remover as linhas completas e "descer" as linhas acima delas
        linhas_remover.sort()

        for lin in linhas_remover:
            for i in range(lin, 0, -1):  
                for j in range(self.num_colunas):  
                    self.matriz_jogo[i][j] = self.matriz_jogo[i - 1][j]  # substitui pela linha acima
        
        # limpar a primeira linha
        for j in range(self.num_colunas):
            self.matriz_jogo[0][j] = " "
        
        # esquema de pontuação
        pontos = 0
        if(len(linhas_remover) == 1):
            pontos = 1
        elif(len(linhas_remover) == 2):
            pontos = 3
        elif(len(linhas_remover) == 3):
            pontos = 5
        elif(len(linhas_remover) >= 4):
            pontos = 7

        self.pontuacao += pontos
        self.jogador.atualizar_pontuacao(pontos)

    def verifica_fim_de_jogo(self, matriz_peça, pos_x_peça, pos_y_peça):
        """
        Verifica se alguma peça está no centro e no topo da matriz
        se não for possível adicionar uma nova peça sem que ela colida
        """

        if Movimento.pode_colocar_na_posicao(matriz_peça, self.matriz_jogo, pos_x_peça, pos_y_peça):
            self.partida_rodando = True
        
        else:
            self.partida_rodando = False

    
    def movimento_vertical(self):
        """
        se possível move a peça para baixo e desenha na matriz do jogo
        """
        if Movimento.pode_mover_para_baixo(self.peça_atual.matriz_peça, self.matriz_jogo, self.peça_atual.pos_x, self.peça_atual.pos_y):
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
        if direçao == "direita" and Movimento.pode_mover_para_direita(self.peça_atual.matriz_peça, self.matriz_jogo, self.peça_atual.pos_x, self.peça_atual.pos_y):
            self.apaga_peça_na_matriz()
            self.peça_atual.pos_y += 1 
            self.desenha_peça_na_matriz()

        elif direçao == "esquerda" and Movimento.pode_mover_para_esquerda(self.peça_atual.matriz_peça, self.matriz_jogo, self.peça_atual.pos_x, self.peça_atual.pos_y):
            self.apaga_peça_na_matriz()
            self.peça_atual.pos_y -= 1  
            self.desenha_peça_na_matriz()


    def movimento_rotaciona(self,direçao):
        """
        rotaciona a peça atual 90° para a direita ou para a esquerda
        """

        self.peça_auxiliar = Peça(self.peça_atual.pos_x, self.peça_atual.pos_y)
        matriz_atual_peça = self.peça_auxiliar.matriz_peça = Matriz.copia_matriz(self.peça_atual.matriz_peça)

        # Rotações baseadas na direção
        if direçao == "direita":
            nova_matriz_rotacionada = self.peça_auxiliar.rotacionar_direita(matriz_atual_peça)
        elif direçao == "esquerda":
            nova_matriz_rotacionada = self.peça_auxiliar.rotacionar_esquerda(matriz_atual_peça)

        self.apaga_peça_na_matriz()

        if Movimento.pode_colocar_na_posicao(nova_matriz_rotacionada, self.matriz_jogo, self.peça_auxiliar.pos_x, self.peça_auxiliar.pos_y):
            # aplica a rotação na peça atual
            self.peça_atual.matriz_peça = Matriz.copia_matriz(nova_matriz_rotacionada)
            
            self.peça_atual.pos_x = self.peça_auxiliar.pos_x
            self.peça_atual.pos_y = self.peça_auxiliar.pos_y

        self.desenha_peça_na_matriz()

    def para_partida(self):
        """
        Encerra a partida antes de seu término natural.
        """
        self.partida_rodando = False

    def grava_sai_partida(self):
        """
        Salva o estado atual da partida e encerra.
        """
        time = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"{self.jogador.nome}_{time}.pkl"
        with open(nome_arquivo, "wb") as f:
            pickle.dump(self, f)

        from jogo import Jogo # importação localizada
        Jogo.arquivos_gravados.append(nome_arquivo)
        self.exibe_salvamento = True
        self.para_partida()