import os

class Tela:

    def __init__(self, matriz_partida):
        self.matriz_tela = matriz_partida

    def exibe_matriz(self):
        """exibe a matriz do jogo no terminal com as grades"""
        self.limpa_tela()

        print("+" + "-" * (len (self.matriz_tela[0])) + "+")  

        for linha in self.matriz_tela:
            linha_formatada = "|"
            for caracter in linha:
                linha_formatada += caracter
            linha_formatada += "|"
            print(linha_formatada)

        print("+" + "-" * (len (self.matriz_tela[0])) + "+")  

    def exibe_comandos(self, pontuacao):
        """exibe as instruções do jogo """

        print("\nPontuação:", pontuacao)
        print("Teclas do jogo:")
        print("← move esquerda | → move direita | ↓ move baixo")
        print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
        print("<s> sai da partida | <g> grava e sai da partida")


    def exibe_comandos_game_over(self, pontuacao):
        print("Fim da partida!")
        print("Pontuação final:", pontuacao)
        print("\n*** Jogo Textris - um tetris em modo texto ***")
        
    def limpa_tela(self):
        """limpa o terminal para atualizar a visualização do jogo """
        os.system('cls || clear')