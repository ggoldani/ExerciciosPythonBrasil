import math

area = eval(input('Informe a área a ser pintada (em m²): '))
area_a_ser_pintada = area * 1.1
litros = area_a_ser_pintada / 6
custo_lata = 80
litro_lata = 18
custo_galao = 25
litro_galao = 3.6

quantidade_apenas_lata = math.ceil(litros / litro_lata)
custo_apenas_lata = quantidade_apenas_lata * custo_lata

if quantidade_apenas_lata == 1:
    print(f'Usando apenas latas, será necessária {quantidade_apenas_lata} lata com custo de R${custo_apenas_lata:.2f}.')
elif quantidade_apenas_lata > 1:
    print(f'Usando apenas latas, será necessária {quantidade_apenas_lata} lata com custo de R${custo_apenas_lata:.2f}.')

quantidade_apenas_galao = math.ceil(litros / litro_galao)
custo_apenas_galao = quantidade_apenas_galao * custo_galao

if quantidade_apenas_galao == 1:
    print(f'Usando apenas galões, será necessário {quantidade_apenas_galao} galão com custo de R${custo_apenas_galao:.2f}.')
elif quantidade_apenas_galao > 1:
    print(f'Usando apenas galões, serão necessários {quantidade_apenas_galao} galões com custo de R${custo_apenas_galao:.2f}.')

quantidade_lata = math.floor(litros / litro_lata)
litros_que_faltam = litros % litro_lata
quantidade_galao = math.ceil(litros_que_faltam / litro_galao)
custo_total = quantidade_lata * custo_lata + quantidade_galao * custo_galao

print('Usando latas e galões ', end = '')
if quantidade_lata == 1:
    print(f'será necessária {quantidade_lata} lata ', end = '')
elif quantidade_lata > 1:
    print(f'serão necessárias {quantidade_lata} latas ', end='')

if quantidade_galao == 1:
    print(f'e {quantidade_galao} galão ', end='')
elif quantidade_galao > 1:
    print(f'e {quantidade_galao} galões ', end='')

print(f'com custo total de R${custo_total:.2f}.')