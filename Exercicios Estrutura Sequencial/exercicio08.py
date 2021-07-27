'''
Calculo de ganho mensal
'''

valor_hora = eval(input('Informe o valor da hora trabalhada R$: '))
horas_trabalhadas = eval(input('Informe quantas horas foram trabalhadas no mes: '))

salario = valor_hora * horas_trabalhadas

print(f'O seu salario no mes sera de R${salario:.2f}.')