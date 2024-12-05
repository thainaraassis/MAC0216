class Ranking:

    ranks = []

    def exibir_rankings(self):
        """
        Mostra as melhores pontuações já alcançadas no jogo em execução.
        """

        print("\n*** Ranking ***")

        # iremos ordenar a lista de ranks por pontuação dos jogadores, da maior para a menor
        self.ranks.sort(key=lambda jogador: jogador.pontuacao, reverse=True)

        if not self.ranks:
            print("Nenhuma pontuação registrada ainda.\n")
            return
        else:
            # f-strings
            # f"{valor:preenchimento<largura}"
            print(f"{'Posição':<10}{'Jogador':<10}{'Pontuação':<10}")
            print("-" * 40)

            for i in range(min(len(self.ranks), 10)):
                print(f"{i+1:<10}{self.ranks[i].nome:<10}{self.ranks[i].pontuacao:<10}")
            
            print("\n")