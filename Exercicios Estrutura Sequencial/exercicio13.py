'''
peso ideal para homens e para mulheres
'''

altura = eval(input('Informe a sua altura em metros: '))
sexo = input('Informe seu sexo (F para feminino e M para masculino): ')

while not sexo in "MmFf":
    sexo = input('Sexo invalido. Informe seu sexo (F para feminino e M para masculino): ')

peso_ideal_masculino = (72.7 * altura) - 58
peso_ideal_feminino = (62.1 * altura) - 44.7

if sexo in "Ff":
    print(f'Seu peso ideal: {peso_ideal_feminino:.2f}Kg')
elif sexo in "Mm":
    print(f'Seu peso ideal: {peso_ideal_masculino:.2f}Kg')
else:
    print('Sexo invalido')