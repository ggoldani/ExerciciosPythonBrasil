'''
Exercicio 10 da lista de classes do python brasil
'''

class BombaCombustivel:
    def __init__(self, tipo, valor_litro, quantidade_combustivel):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def AbasterPorValor(self, valor_abastecido):
        self.valor_abastecido = valor_abastecido

    def AbastecerPorLitro(self, litros_abastecidos):

    def AlterarValorLitro(self, valor_litro):
        self.valor_litro = valor_litro