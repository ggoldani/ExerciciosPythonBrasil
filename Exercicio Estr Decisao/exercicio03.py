letra = input('Digite a lera correspondente ao seu sexo, sendo F para feminino e M para masculino: ')

while True:
    if letra in "Ff":
        print('Letra F digitada. Feminino.')
        break
    elif letra in "Mm":
        print('Letra M digitada. Masculino.')
        break
    else:
        print('Letra invalida.')
        letra = input('Digite uma letra valida, F ou M: ')