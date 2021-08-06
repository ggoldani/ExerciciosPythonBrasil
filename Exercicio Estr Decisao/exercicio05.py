nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media >= 10:
    print(f'Média {media:.2f}. Aprovado com distinção.')
elif 10 > media >= 7:
    print(f'Média {media:.2f}. Aprovado.')
elif media < 7:
    print(f'Média {media:.2f}. Reprovado')
