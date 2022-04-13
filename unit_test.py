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
    lado = 6
    resultado_esperado = 200

    # Executa
    resultado_obtido = main.calcular_area_cubo(lado)

    # Valida
    assert resultado_esperado == resultado_obtido

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
    (16, '', '')
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar_area)
def test_calcular_area_paralelograma(numero1, numero2, resultado_esperado):
    # Configura
    # Executa
    resultado_obtido = main.calcular_area_paralelograma(numero1, numero2)

    # Valida
    assert resultado_obtido == resultado_esperado

@pytest.mark.parametrize('id, numero1, numero2, resultado_esperado, tipo_teste', ler_dados_csv())
def test_area_da_piramide(id, numero1, numero2, resultado_esperado, tipo_teste):
    # Configura
    # Executa
    resultado_obtido = main.calcular_area_piramide(int(numero1), int(numero2))

    # Valida
    if tipo_teste == 'negativo':
        assert resultado_obtido == str(resultado_esperado)  # Teste Negativo
    else:
        assert float(resultado_obtido) == float(resultado_esperado)  # Teste Positivo
