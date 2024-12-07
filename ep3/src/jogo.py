from partida import Partida
from ranking import Ranking
import pickle
import os

class Jogo:

    arquivos_gravados =[]

    def __init__(self):
        self.partida = None

    def menu(self):
        print("*** Jogo Textris - um tetris em modo texto ***")
        while True:
            print("Opções do jogo:")
            print("- <i> Iniciar uma nova partida")
            print("- <c> Carregar uma partida gravada e continuá-la")
            print("- <p> Ver as 10 melhores pontuações")
            print("- <s> Sair do jogo")
            opçao = input("Digite a opção desejada: ").strip().lower()

            if opçao == "i":
                self.iniciar_partida()
            elif opçao == "c":
                self.carregar_partida()
            elif opçao == "p":
                self.exibir_rankings()
            elif opçao == "s":
                self.sair_jogo()
                break
            else:
                print("Opção inválida!")
    
    def iniciar_partida(self):

        nome_jogador = input("Digite o nome do jogador: ")
        num_linhas = input("Digite o número de linhas da tela do jogo: ")
        num_colunas = input("Digite o número de colunas da tela do jogo: ")
        self.partida = Partida(nome_jogador, num_linhas, num_colunas)
        self.partida.jogar()
    
    def carregar_partida(self):
        """
        Carrega uma partida salva anteriormente.
        """
        if not self.arquivos_gravados:
            print("\nNão há partidas salvas.\n")
            return
        else:
            print("\nPartidas salvas:\n")
            for item in self.arquivos_gravados:
                print(item)

            nome_arquivo = input("\nDigite o nome da partida que deseja retomar:\n")

            if os.path.exists(nome_arquivo):
                with open(nome_arquivo, "rb") as f:
                    self.partida = pickle.load(f)
                self.partida.jogar()
            else:
                print("\nEssa partida não existe.\n")

    def exibir_rankings(self):
        ranking = Ranking()  
        ranking.exibir_rankings()

    def sair_jogo(self):
        """
        Exclui todos os arquivos .pkl no diretório atual.
        """
        for arq in self.arquivos_gravados:
            os.remove(arq)