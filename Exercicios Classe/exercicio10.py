'''
Exercicio 10 da lista de classes do python brasil
'''

class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, quantidade_combustivel:float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abasterPorValor(self, valor_abastecido:float):
        litrosAbastecidos = valor_abastecido / self.valor_litro
        self.quantidade_combustivel -= litrosAbastecidos
        return print(f'Foram abastecidos {litrosAbastecidos:.2f} litros e sobraram {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel} na bomba.')

    def abastecerPorLitro(self, litros_abastecidos:float):
       valor_abastecido = litros_abastecidos * self.valor_litro
       self.quantidade_combustivel -= litros_abastecidos
       return print(f'O valor a ser pago eh de R$ {valor_abastecido:.2f} e sobram {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel} na bomba.')

    def alterarValorLitro(self, valor_litro):
        self.valor_litro = valor_litro
        return print(f'Valor do litro atualizado, novo valor R$ {self.valor_litro:.2f}.')

    def alterarQuantidadeCombustivel(self, litros_adicionados):
        self.quantidade_combustivel += litros_adicionados
        return print(f'Litros totais na bomba: {self.quantidade_combustivel:.2f} L.')

bomba = BombaCombustivel("Alcool", 4.09, 1000.00)

valor_abastecido = float(input('Valor a ser abastecido: R$'))
bomba.abasterPorValor(valor_abastecido)

litros_abastecidos = float(input('Litros a serem abastecidos: R$'))
bomba.abastecerPorLitro(litros_abastecidos)

trocar_valor_litro = input(f'Senhor gerente, deseja alterar o valor do litro do combustivel atual S/N? ')
if trocar_valor_litro in "Ss":
    novo_valor_litro = float(input('Informe o novo valor: R$'))
    bomba.alterarValorLitro(novo_valor_litro)

alterar_quantidade_comustivel = input(f'Deseja alterar a quantidade atual de combustivel S/N? ')
if alterar_quantidade_comustivel in "Ss":
    quantidade_adicionada = float(input('Informe a quantidade de litros a ser adicionada: '))
    if quantidade_adicionada < 0:
       print('Eh proibida a retirada de combustivel.')
    else:
        bomba.alterarQuantidadeCombustivel(quantidade_adicionada)

print('Finalizar programa.')