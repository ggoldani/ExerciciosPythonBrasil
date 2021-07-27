'''
Exercicio 01 da lista de classes do python brasil
'''

class ModeloBola: #classe sempre se inicia com letra maiuscula e usa camelcase
    def __init__(self): # __init__ cria os atributos de dados dos objetos, self eh o proprio objeto
        self.cor = 'azul'
        self.circunferencia = 4
        self.material = 'plastico'

    def troca_cor(self, cor): # "funcoes" dentro de classes sao os metodos
        self.cor = cor
        return self.cor

    def mostra_cor(self):
        return self.cor

bola_01 = ModeloBola()
bola_02 = ModeloBola()

bola_01.troca_cor('verde')
bola_01.circunferencia = 5
bola_01.material = 'couro'
print(bola_01.mostra_cor(), bola_01.circunferencia, bola_01.material)

bola_02.troca_cor('vermelho')
bola_02.circunferencia = 10
bola_02.material = 'papel'
print(bola_02.mostra_cor(), bola_02.circunferencia, bola_02.material)
