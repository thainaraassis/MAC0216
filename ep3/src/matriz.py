class Matriz:

    @staticmethod
    def devolve_matriz_vazia(num_linhas,num_colunas):

        matriz_inicial = []  

        for _ in range(num_linhas):  
            linha = []  
            for _ in range(num_colunas):  
                linha.append(" ")  
            matriz_inicial.append(linha)  

        return matriz_inicial
    
    @staticmethod
    def copia_matriz(matriz_ref):

        matriz_copia = []  

        for i in range(len(matriz_ref)):  
            linha = []  
            for j in range(len(matriz_ref[0])):  
                linha.append(matriz_ref[i][j])  

            matriz_copia.append(linha)  

        return matriz_copia