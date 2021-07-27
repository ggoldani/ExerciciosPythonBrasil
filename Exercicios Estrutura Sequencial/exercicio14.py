'''
Calculo da multa por excesso de peixes
'''

peso_peixes = eval(input('Informe o peso de peixes em kg: '))
excesso = peso_peixes - 50
multa = excesso * 4

if excesso <= 0:
    print('Nao ha excesso, nao ha multa.')
else:
    print(f'Houve excesso de {excesso}kg de peixe. Multa aplicada de R${multa:.2f}.')