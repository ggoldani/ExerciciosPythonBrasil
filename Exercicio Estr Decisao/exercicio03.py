letra = input('Digite a lera correspondente ao seu sexo, sendo F para feminino e M para masculino: ').upper()

while True:
    if letra == "F":
        print('Letra F digitada. Feminino.')
        break
    elif letra == "M":
        print('Letra M digitada. Masculino.')
        break
    else:
        print('Letra invalida.')
        letra = input('Digite uma letra valida, F ou M: ')