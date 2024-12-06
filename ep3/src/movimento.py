class Movimento:

    @staticmethod
    def pode_mover_para_esquerda(matriz_da_peça, matriz_do_jogo, pos_x_peça, pos_y_peça):
        """
        Verifica se a peça pode se mover para a esquerda.
        """
        for i in range(len(matriz_da_peça)):  
            for j in range(len(matriz_da_peça[0])):  
                if matriz_da_peça[i][j] != " ":  
                    coluna_a_esquerda = j - 1  

                    # verifica as células na borda esquerda ou que possuem " " à esquerda na peça
                    if coluna_a_esquerda < 0 or matriz_da_peça[i][coluna_a_esquerda] == " ":
                        x = pos_x_peça + i  # coordenada x na matriz do jogo
                        y = pos_y_peça + j - 1  # coordenada y na matriz do jogo

                        # verifica limites ou colisão
                        if y < 0 or matriz_do_jogo[x][y] != " ":
                            return False  

        return True  

    @staticmethod
    def pode_mover_para_direita(matriz_da_peça, matriz_do_jogo, pos_x_peça, pos_y_peça):
        """
        Verifica se a peça pode se mover para a direita.
        """
        for i in range(len(matriz_da_peça)):  
            for j in range(len(matriz_da_peça[0])):  
                if matriz_da_peça[i][j] != " ": 
                    coluna_a_direita = j + 1  

                    # verifica as células na borda direita ou que possuem " " à direita na peça
                    if coluna_a_direita >= len(matriz_da_peça[0]) or matriz_da_peça[i][coluna_a_direita] == " ":
                        x = pos_x_peça + i  # coordenada x na matriz do jogo
                        y = pos_y_peça + j + 1  # coordenada y  na matriz do jogo

                        # verifica limites ou colisão
                        if y >= len(matriz_do_jogo[0]) or matriz_do_jogo[x][y] != " ":
                            return False  
        return True 

    @staticmethod
    def pode_mover_para_baixo(matriz_da_peça, matriz_do_jogo, pos_x_peça, pos_y_peça):
        """
        verifica se a peça pode se mover para baixo
        """
        for i in range(len(matriz_da_peça)):  
            for j in range(len(matriz_da_peça[0])):  
                
                if matriz_da_peça[i][j] != " ":  
                    proxima_linha_peça = i + 1  

                    # verifica as células da peça que estão na última linha ou
                    # as que abaixo é vazio
                    if ((proxima_linha_peça >= len(matriz_da_peça))
                        or (matriz_da_peça[proxima_linha_peça][j] == " ")):

                        # verifica a célula abaixo na matriz do jogo
                        x = pos_x_peça + i + 1  
                        y = pos_y_peça + j  

                        # colide com outra peça ou a grade
                        if x >= len(matriz_do_jogo) or matriz_do_jogo[x][y] != " ":
                            return False

        return True  

    @staticmethod
    def pode_colocar_na_posicao(nova_matriz_peça, matriz_do_jogo, nova_pos_x, nova_pos_y):
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
                    if x < 0 or x >= len(matriz_do_jogo) or y < 0 or y >= len(matriz_do_jogo[0]):
                        return False

                    # Verifica colisão com outra peça
                    if matriz_do_jogo[x][y] != " ":
                        return False
        return True
