'''
Exercicio 03 da lista de classes do python brasil
'''

class Retangulo:
    def __init__(self, lado_A = 1, lado_B = 1):
        self.lado_A = lado_A
        self.lado_B = lado_B

    def mudar_lados(self, lado_A, lado_B):
        self.lado_A = lado_A
        self.lado_B = lado_B

    def retornar_lados(self):
        return self.lado_A, self.lado_B

    def retornar_area(self):
        return self.lado_A * self.lado_B

    def retornar_perimetro(self):
        return self.lado_A + self.lado_B

lado_01 = eval(input('Informe a lateral do local em metros: '))
lado_02 = eval(input('Informe a outra lateral do local tambem em metros: '))

retangulo = Retangulo(lado_01, lado_02)

print(f'A quantidade de piso necessaria sera de {retangulo.retornar_area():.2f} m² e a quantidade de rodape sera de {retangulo.retornar_perimetro()} m.')

