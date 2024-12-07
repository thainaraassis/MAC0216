class Jogador:
    
    def __init__(self, nome, pontuacao=0):
        self.nome = nome
        self.pontuacao = pontuacao

    def atualizar_pontuacao(self, pontos):
        self.pontuacao += pontos