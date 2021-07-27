'''
Calculando salario bruto e liquido com descontos
Imposto de renda 11% do bruto
INSS 8% do bruto
Sindicato 5% do bruto
'''

valor_hora = eval(input('Informe o valor da hora trabalhada R$'))
horas_mes = eval(input('Informe quantas horas foram trabalhadas no mes: '))

salario_bruto = valor_hora * horas_mes
desconto_imposto_de_renda = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - desconto_sindicato - desconto_inss - desconto_imposto_de_renda

print(f'''
Dados do salario e descontos

Salario bruto:   R${salario_bruto:.2f}
Desconto IR:     R${desconto_imposto_de_renda:.2f}
Desconto INSS:   R${desconto_inss:.2f}
Desconto Sind.:  R${desconto_sindicato:.2f}

Salario liquido: R${salario_liquido:.2f}
''')