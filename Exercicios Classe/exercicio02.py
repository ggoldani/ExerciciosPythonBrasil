'''
Exercicio 02 da lista de classes do python brasil
'''

class ModeloQuadrado:
    def __init__(self, lado = 1): # lado = 1 indica o valor padrao caso nao seja passado nenhum valor
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

quadrado = ModeloQuadrado(4) # passando diretamente um valor para a classe, ele passa o valor para o init

print(quadrado.lado, quadrado.calcular_area())