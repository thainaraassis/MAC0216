from partida import Partida

class Jogo:

    def menu(self):
        print("*** Jogo Textris - um tetris em modo texto ***")
        while True:
            print("\nOpções do jogo:")
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
                print("Sai do jogo. Implementar alguma coisa?")
                break
            else:
                print("Opção inválida!")
    
    def iniciar_partida(self):

        nome_jogador = input("Digite o nome do jogador: ")
        num_linhas = input("Digite o número de linhas da tela do jogo: ")
        num_colunas = input("Digite o número de colunas da tela do jogo: ")
        partida = Partida(nome_jogador, num_linhas, num_colunas)
        partida.jogar()
    
    def carregar_partida(self):
         """
         abre arquivo com o jogador, a pontuação, a matriz e etc
         """

    def exibir_rankings(self):
         """
         abre arquivo com todas as pontuações salvas e os respectivos jogadores e data?
         """