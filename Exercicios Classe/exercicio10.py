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
        if litrosAbastecidos < self.quantidade_combustivel:
            self.quantidade_combustivel -= litrosAbastecidos
            return print(f'Foram abastecidos {litrosAbastecidos:.2f} litros e sobraram {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel} na bomba.')
        else:
            print('N�o h� combustivel suficiente.')

    def abastecerPorLitro(self, litros_abastecidos:float):
        if litros_abastecidos < self.quantidade_combustivel:
            valor_abastecido = litros_abastecidos * self.valor_litro
            self.quantidade_combustivel -= litros_abastecidos
            return print(f'O valor a ser pago eh de R$ {valor_abastecido:.2f} e sobram {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel} na bomba.')
        else:
            print('N�o h� quantidade de combustivel suficiente.')

    def alterarValorLitro(self, valor_litro):
        self.valor_litro = valor_litro
        return print(f'Valor do litro de {self.tipo_combustivel} atualizado, novo valor R$ {self.valor_litro:.2f}.')

    def alterarQuantidadeCombustivel(self, litros_adicionados):
        self.quantidade_combustivel += litros_adicionados
        return print(f'Litros adicionados: {litros_adicionados}\nLitros totais na bomba: {self.quantidade_combustivel:.2f} L.')

tipo_combustivel = input('Informe o tipo de combustivel da bomba (Alcool ou Gasolina): ')
valor_litro = float(input('Informe o valor por litro R$'))
quantidade_combustivel = float(input('Quantidade de combustivel em estoque: '))
bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

i = 1

while True:
    print(f'======= Cliente {i} =======')

    litro_ou_valor = input('Tipo de abastecimento:\n1 - Por valor\n2 - Por litro\n')

    if litro_ou_valor == '1':
        valor_abastecido = float(input('Valor a ser abastecido: R$'))
        bomba.abasterPorValor(valor_abastecido)
    elif litro_ou_valor == '2':
        litros_abastecidos = float(input('Litros a serem abastecidos: '))
        bomba.abastecerPorLitro(litros_abastecidos)
    else:
        print('Opç�o inv�lida.')

    trocar_valor_litro = input(f'Deseja alterar o valor do litro do combustivel atual S/N? ')
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

    encerrar = input('Encerrar? S/N ')
    if encerrar in "Ss":
        break
    i += 1

print('Programa finalizado.')