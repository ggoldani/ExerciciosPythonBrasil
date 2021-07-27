'''
Exercicio 05 da lista de classes do python brasil
'''

class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo = 0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome
        return f'Nome alterado para: {self.nome}.'

    def deposito(self, deposito):
        self.saldo += deposito
        return f'Deposito de R${deposito:.2f} efetudo. Novo saldo: R${self.saldo:.2f}'

    def saque(self, saque):
        self.saldo -= saque
        return f'Saque de R${saque:.2f} efetudo. Novo saldo: R${self.saldo:.2f}'

cliente = input('Digite nome do cliente: ')
num_conta = eval(input('Informe o numero da conta: '))
saldo_atual = eval(input('Informe o saldo atual: '))

gustavo = ContaCorrente(num_conta, cliente, saldo_atual)

realizar_deposito = input('Deseja realizar deposito? S - Sim, N - Nao ')

if realizar_deposito in "Ss":
   valor_deposito = eval(input('Qual eh o valor do deposito? R$'))
   gustavo.saldo += valor_deposito
   print(f'Depositos realizados. Novo saldo: R${gustavo.saldo:.2f}.')

realizar_saque = input('Deseja realizar saque? S - Sim, N - Nao ')
if realizar_saque in "Ss":
    valor_saque = eval(input('Qual eh o valor do saque? R$'))
    if valor_saque > gustavo.saldo:
        print('Erro! Valor do saque superior ao saldo.')
    else:
        gustavo.saldo -= valor_saque
        print(f'Saque realizado. Novo saldo: R${gustavo.saldo:.2f}.')

