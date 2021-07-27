'''
Graus Fahrenheit em Graus Celsius
'''

temp_f = eval(input('Informe a temperatura em Fahrenheit: '))

temp_c = 5 * ((temp_f-32) / 9)

print(f'{temp_f}F = {temp_c:.2f}ºC')