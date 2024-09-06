import json

def calcular_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

def pertence_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def analise_faturamento(dados_json):
    dados = json.loads(dados_json)
    faturamento = dados["faturamento"]
    valores = list(faturamento.values())

    menor_valor = min(valores)
    maior_valor = max(valores)

    dias_com_faturamento = [v for v in valores if v > 0]
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for v in dias_com_faturamento if v > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

def calcular_percentuais(faturamento_estado):
    total = sum(faturamento_estado.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estado.items()}
    return percentuais

def inverter_string(s):
    s_invertida = ''
    for char in s:
        s_invertida = char + s_invertida
    return s_invertida

indice = 13
soma = calcular_soma(indice)
print(f"Soma dos primeiros {indice} números naturais: {soma}")

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

dados_json = '''
{
    "faturamento": {
        "01": 220.00,
        "02": 230.00,
        "03": 250.00,
        "04": 0.00,
        "05": 270.00,
        "06": 300.00,
        "07": 0.00,
        "08": 260.00,
        "09": 0.00,
        "10": 240.00
    }
}
'''
menor_valor, maior_valor, dias_acima_media = analise_faturamento(dados_json)
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media}")

faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
percentuais = calcular_percentuais(faturamento_estado)
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

string = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")
