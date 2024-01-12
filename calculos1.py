from requests import get

x = get('https://archive-api.open-meteo.com/v1/archive?latitude=-32.0332&longitude=-52.0986&start_date=2022-12-22&end_date=2023-03-20&daily=temperature_2m_mean,apparent_temperature_mean,windspeed_10m_max,winddirection_10m_dominant&timezone=America%2FSao_Paulo')
rg = x.json()

def media(dados):
    med =(sum(dados)/len(dados))
    return med
def desvio(dados):
    d = [(x - media(dados))**2 for x in dados]
    variancia = sum(d)/len(dados)
    desvio = (variancia)**0.5
    return desvio

medrg = media(rg["daily"]["temperature_2m_mean"])
'''calcula a média da temperatura medida'''
medrg2 = media(rg["daily"]["apparent_temperature_mean"])
'''calcula a média da temperatura aparente'''
print(f"A média calculada de temperatura medida para cidade de Rio Grande é igual a {medrg}°C ")
print(f"A média calculada de temperatura aparente para cidade de Rio Grande é igual a {medrg2}°C")
#
desv = desvio(rg["daily"]["temperature_2m_mean"])
'''calcula o desvio padrão da temperatura medida'''
desv2 = desvio(rg["daily"]["apparent_temperature_mean"])
'''calcula o desvio padrão da temperatura aparente'''

print(f"O desvio padrão calculado de temperatura medida para cidade de Rio Grande é igual a {desv}°C")
print(f"O desvio padrão calculado de temperatura aparente para cidade de Rio Grande é igual a {desv2}°C")
#
direct = (rg["daily"]["winddirection_10m_dominant"])
'''variável com o nome de direct que procura no dicionário daily as direções dominantes'''
day = rg["daily"]["time"]
'''
variável responsável por buscar no dicionário o dia
'''

win = (rg["daily"]["windspeed_10m_max"])
'''variável com nome de win que procura no dicionário daily as direções de vento máximo'''

win_max = max(win)
'''variável com nome de win_max que procura dentro da variável win o valor máximo utilizando a função max'''

win_max_index = win.index(win_max)
'''variavel win_max_index seleciona a variavel win_max com o index o vento maximo'''

max_direct = direct[win_max_index]
'''index da direção de vento máxima'''


print(f" A direção náutica respectiva para o dia encontrado é de:", (rg["daily"]["winddirection_10m_dominant"][win_max_index]))
'''
Calcular da mesma forma utilizando index para encontrar o dia de vento máximo
'''

print(f"O dia de vento máximo foi", (rg["daily"]["time"][win_max_index]))

temp_ap = rg["daily"]["temperature_2m_mean"]
temp_ab = rg["daily"]["apparent_temperature_mean"]

'''variavel que armazena as datas correspondentes ao período de solicitação do script'''

time = rg["daily"]["time"]
'''Calcula a diferença absoluta a partir do método abs tendo como parametro x - y
para cada x, y em zip(método responsável por combinar itens de duas ou mais listas) que recebe como parâmetro as variáveis temp_ap e temp_ab (de temperatura medida e temperatura aparente)'''

diferenca = [abs(x - y) for x, y in zip(temp_ap, temp_ab)]

'''variável diferença máxima que retorna o valor máximo da variável diferença(onde foi calculado o valor absoluto)'''

diferenca_max = max(diferenca)
'''diferença máxima index seleciona o índice onde se encontra o valor máximo da variável anterior'''

diferenca_max_index = diferenca.index(diferenca_max)

print(f"A maior diferença absoluta entre temperatura medida e temperatura aparente é igual a {diferenca_max}°C")

print(f"O dia relativo a maior diferença absoluta foi", (rg["daily"]["time"][diferenca_max_index]))