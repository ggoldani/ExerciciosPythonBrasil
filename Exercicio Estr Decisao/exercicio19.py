numero = eval(input('Digite um numero inteiro positivo menor que 1000: '))

centenas_str = dezenas_str = unidades_str = ''
partes_numericas = 0

centenas_int, numero = divmod(numero, 100)

if centenas_int == 1:
    centenas_str = '1 centena'
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'
    partes_numericas += 1

dezenas_int, numero = divmod(numero, 10)

if dezenas_int == 1:
    dezenas_str = '1 dezena'
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'
    partes_numericas += 1

if numero == 1:
    unidades_str = '1 unidade'
    partes_numericas += 1
elif numero > 1:
    unidades_str = f'{numero} unidades'
    partes_numericas += 1

if partes_numericas == 0:
    print('O numero 0 não possui centenas, dezenas ou unidades.')
elif partes_numericas == 1:
    print(f'{centenas_str + dezenas_str + unidades_str}.')
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}.')
elif partes_numericas == 2:
    if centenas_str != '':
        print(f'{centenas_str} e {dezenas_str + unidades_str}.')
    else:
        print(f'{dezenas_str} e {unidades_str}.')

