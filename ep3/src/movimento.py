class Movimento:

    @staticmethod
    def pode_mover_para_esquerda(matriz_da_peça, matriz_do_jogo, pos_x_peça, pos_y_peça):
        """
        verifica se a peça pode se mover para a esquerda
        """
        primeira_coluna_peça = 0

        for i in range(len(matriz_da_peça)):
            if matriz_da_peça[i][primeira_coluna_peça] != " ":
                x = pos_x_peça + i
                y = pos_y_peça + primeira_coluna_peça - 1  

                # colide com outra peça ou a grade à esquerda
                if y < 0 or matriz_do_jogo[x][y] != " ":
                    return False  
        return True

    @staticmethod
    def pode_mover_para_direita(matriz_da_peça, matriz_do_jogo, pos_x_peça, pos_y_peça):
        """
        verifica se a peça pode se mover para a direita
        """
        ultima_coluna_peça = len(matriz_da_peça[0]) - 1

        for i in range(len(matriz_da_peça)):              
            if matriz_da_peça[i][ultima_coluna_peça] != " ":  
                x = pos_x_peça + i  
                y = pos_y_peça + ultima_coluna_peça + 1  

                # colide com outra peça ou a grade à direita
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
