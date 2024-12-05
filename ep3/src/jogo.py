from partida import Partida
import pickle

class Jogo:

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
                print("Sai do jogo. Implementar alguma coisa? Sim, exlcuir os .pkl")
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
        if not self.partida:
            print("\nComece uma partida primeiro!\n")
            return
        elif self.partida.nome_arquivo == " ":
            print("\nNão há partidas salvas.\n")
            return
        else:
            with open(self.partida.nome_arquivo, "rb") as f:
                self.partida = pickle.load(f)
            self.partida.jogar()

    def exibir_rankings(self):
         """
         abre arquivo com todas as pontuações salvas e os respectivos jogadores e data?
         """

    # def sair_jogo(self):
      #  """
       # Exclui todos os arquivos .pkl no diretório atual.
        #"""