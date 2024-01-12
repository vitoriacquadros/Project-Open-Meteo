from requests import get

'''
Inicialmente são criadas duas funções genéricas para calcular a categoria do vento a partir de uma variável que mantém armazenado os valores com uma simples estrutura de condição if/elif
Para cada valor de vento ele verifica se é menor que a estrutura de categorias propostas no exercício.

A segunda função irá realizar os cálculos baseando-se na analise em que:
Se a direçao(variável que armazena os valores) for maior ou igual aos valor de graus - 22.5 E a direção for menor ou igual a graus + 22.5 ele irá retornar com o indíce da variavel nautica (lista criada com o nome de cada direção)

'''

dados = get("https://archive-api.open-meteo.com/v1/archive?latitude=-32.0332&longitude=-52.0986&start_date=2022-12-22&end_date=2023-03-20&daily=temperature_2m_mean,apparent_temperature_mean,windspeed_10m_max,winddirection_10m_dominant&timezone=America%2FSao_Paulo")

leitura = dados.json()


def cat_win(v):
        if v < 3.6:
            return 0
        elif v < 7.2:
            return 1
        elif v < 10.8:
            return 2
        elif v < 18.0:
            return 3
        elif v < 28.8:
             return 4
        elif v < 36.0:
            return 5
        elif v < 40.0:
            return 6


def nautica(direcao):
    nautica = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    graus = [0, 45, 90, 135, 180, 225, 270, 315]

    for i in range(len(nautica)):
        if (direcao >= graus[i] - 22.5) and (direcao <= graus[i] + 22.5):
         return nautica[i]



l = []
linha = ''

'''
Essa estrutura for percorre a lista de valores que contenham a data diretamente do provedor de webservice.
São criadas as cinco primeiras variáveis baseadas nas informações contidas no provedor
A duas ultimas são chamadas das funções anteriores para categorizar o vento e sua direção nautica.

Quando a função cat_win é chamada, ela verifica se o valor percorrido em ["daily"]["windspeed_10m_max"] satisfaz algum dos valores contidos na função.
Se sim, o próximo passado será chamar a função dir_nautica e fazer a leitura dos valores em ''direcao''
Ela irá percorrer toda lista e condicionar se satisfaz as duas condições da função. Ser maior ou igual aos graus somando e diminuindo o valor de 22.5

'''
for i in range(len(leitura["daily"]["time"])):
    date = leitura["daily"]["time"][i]
    medida = leitura["daily"]["temperature_2m_mean"][i]
    aparente = leitura["daily"]["apparent_temperature_mean"][i]
    vento = leitura["daily"]["windspeed_10m_max"][i]
    direcao = leitura["daily"]["winddirection_10m_dominant"][i]
    categoria = cat_win(vento)
    dir_nautica = nautica(direcao)

    lista = [date, medida, aparente, vento, direcao, categoria, dir_nautica]
    l.append(lista)

    linha += f'{date};{medida};{aparente};{vento};{direcao};{categoria};{dir_nautica}\n'



arq = open('script2.csv', 'w')
arq.write(linha)
arq.close()
arq = open('script2.csv', 'r')
