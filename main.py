import math

def calcular_area_cubo(lado):
    return (lado*lado)*6

def calcular_area_paralelograma(b,h):
    return (b*h)

def calcular_area_piramide(b,h): # Pirâmide retangular regular - https://brasilescola.uol.com.br/matematica/area-piramide.htm
    try:
        return int(((((math.sqrt((h*h) + (b/2)*(b/2)))*b)/2)*4)+(b*b))
    except TypeError:
        return 'resultado invalido'    # Tratamento de erro


if __name__ == '__main__':
    numero = 6
    resultado = calcular_area_cubo(numero)
    print(f'A área total do cubo é de: {resultado}m2')

    base = 10
    altura = 8
    resultado = calcular_area_paralelograma(base, altura)
    print(f'A área do paralelograma é de {resultado}m2')

    b = 18
    h = 12
    resultado = int(calcular_area_piramide(b, h))
    print(f'A área da pirâmide é de {resultado}m2')