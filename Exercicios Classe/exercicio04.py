'''
Exercicio 04 da lista de classes do python brasil
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self): # encapsulamento
        if self.idade < 21:
            self.altura += 0.05
        self.idade += 1

gustavo = Pessoa('Gustavo', 15, 60, 1.65)

for _ in range(gustavo.idade, 25):
    gustavo.envelhecer()
    print(f'A idade de {gustavo.nome} eh de {gustavo.idade} e sua altura eh de {gustavo.altura}.')