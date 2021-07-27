'''
Calculando quantas latas de tinta para pintar determinada area
'''
import math
area = eval(input('Informe a rea a ser pintada (em m²): '))

litro_tinta = area / 3
lata = litro_tinta / 18
quantidade_latas = math.ceil(lata)
preco_lata = 80
valor_total = quantidade_latas * preco_lata

if quantidade_latas == 1:
    print('Necessaria apenas uma lata no valor de R$80,00.')
else:
    print(f'Usara {quantidade_latas} latas e o custo sera de R${valor_total:.2f}.')