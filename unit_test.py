import main
import pytest
import csv

def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\Particular\\PycharmProjects\\UnitTest_PyTest\\Vendors\\massa_de_testes.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')

def test_calcular_area_cubo_positivo():
    # Configura/Prepara
    lado = 6
    resultado_esperado = 216

    # Executa
    resultado_obtido = main.calcular_area_cubo(lado)

    # Valida
    assert resultado_esperado == resultado_obtido

def test_calcular_area_cubo_negativo():
    # Configura/Prepara
    lado = 'b'
    resultado_esperado = 200

    # Executa
    resultado_obtido = main.calcular_area_cubo(lado)

    # Valida
    try:
        lado01 = int(lado)
        if lado01 > 0:
            return int(resultado_obtido) == int(resultado_esperado)
        else:
            return print('Valor inválido')
    except ValueError:
        return print('Valor inválido')

def test_calcular_area_paralelograma():
    # Configura
    b = 10
    h = 8
    resultado_esperado = 80

    # Executa
    resultado_obtido = main.calcular_area_paralelograma(b, h)

    # Valida
    assert resultado_obtido == resultado_esperado

def test_area_da_piramide():
    # Configura
    b = 18
    h = 12
    resultado_esperado = 864

    # Executa
    resultado_obtido = main.calcular_area_piramide(b, h)

    # Valida
    assert resultado_obtido == resultado_esperado

lista_para_multiplicar_area = [
    (10, 4, 40),
    (15, 'a', 0),
    (16, '', ''),
    ('', 6, 60)
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar_area)
def test_calcular_area_paralelograma(numero1, numero2, resultado_esperado):
    # Configura
    # Executa
    resultado_obtido = main.calcular_area_paralelograma(numero1, numero2)

# Valida
    try:
        numero01 = int(numero1)
        numero02 = int(numero2)
        resultado_esperado_ = int(resultado_esperado)
        if numero01 > 0:
            return resultado_obtido == resultado_esperado
        elif numero02 > 0:
            return resultado_obtido == resultado_esperado
        elif resultado_esperado_ > 0:
            return resultado_obtido == resultado_esperado
        else:
            return print('Valor inválido')
        assert resultado_obtido == resultado_esperado
    except ValueError:
        return print('Valor inválido')

@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())
def test_area_da_piramide(id, numero1, numero2, resultado_esperado, tipo_teste):  # UnitTest CSV
    # Configura
    # Executa
    resultado_obtido = main.calcular_area_piramide(numero1, numero2)

    try:
        numero01 = int(numero1)
        numero02 = int(numero2)
        resultado_esperado_ = int(resultado_esperado)
        if numero01 > 0:
            return resultado_obtido == resultado_esperado_
        elif numero02 > 0:
            return resultado_obtido == resultado_esperado_
        elif resultado_esperado_ > 0:
            return resultado_obtido == resultado_esperado_
        else:
            return print('Valor inválido')
            assert resultado_obtido == resultado_esperado
    except ValueError:
        return print('Valor inválido')
