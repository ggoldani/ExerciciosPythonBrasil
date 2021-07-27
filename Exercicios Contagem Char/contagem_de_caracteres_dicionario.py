#def contar_caracteres(s):
"""Funçao que conta os caracteres de uma string
    Ex:
    >> contar_caracteres(banana)
    {'a': 3, 'b': 1, 'n': 2}
    :param s: string a ser avaliada
    """

''' ############# Soluçao 01 #############

    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    resultado ={}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1
    resultado[caracter_anterior] = contagem
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('gustavo'))
    print()
    print(contar_caracteres('rebecca'))'''

# ############# Solucao 02 #############
def contar_caracteres(s):
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

if __name__ == '__main__':
    print(contar_caracteres('gustavo'))