'''
Media de 4 notas
Maior ou igual a 6, aprovado
Maior ou igual a 4 e menor que 6, recuperacao
Menor que 4, reprovado
'''

n1 = eval(input('Digite a nota do primeiro bimestre: '))
n2 = eval(input('Digite a nota do segundo bimestre: '))
n3 = eval(input('Digite a nota do terceiro bimestre: '))
n4 = eval(input('Digite a nota do quarto bimestre: '))
soma = n1 + n2 + n3 + n4
media = soma / 4

print(f'A media foi {media:.2f}')

if 6 <= media:
    print('Aprovado.')
elif 4 <= media < 6:
    print('Recuperaçao.')
else:
    print('Reprovado.')