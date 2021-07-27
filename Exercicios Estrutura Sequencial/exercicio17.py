import math

area = eval(input('Digite a area a ser pintada em m²: '))
area_com_folga = area * 1.1

litro_tinta = area_com_folga / 6
quantidade_lata = litro_tinta / 18
quantidade_galao = litro_tinta / 3.6
preco_lata = 80
preco_galao = 25

print(f'Usando apenas latas de 18L, sao necessarias {math.ceil(quantidade_lata)}, com custo de R${math.ceil(quantidade_lata)* preco_lata:.2f}. ')
print(f'Usando apenas galoes de 3.6L, sao necessarios {math.ceil(quantidade_galao)}, com custo de R${math.ceil(quantidade_galao * preco_galao):.2f}.')

litros_que_sobram = litro_tinta % 18
valor_total = math.floor(quantidade_lata) * preco_lata + math.ceil(litros_que_sobram / 3.6) * preco_galao

print(f'Usando latas e galoes, sao necessarios {math.floor(quantidade_lata)} latas e {math.ceil(litros_que_sobram / 3.6)} galoes, com valor total de R${valor_total:.2f}.')


