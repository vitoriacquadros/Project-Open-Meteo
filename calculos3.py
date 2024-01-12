from requests import get
from script2 import cat_win, nautica

dados = get("https://archive-api.open-meteo.com/v1/archive?latitude=-32.0332&longitude=-52.0986&start_date=2022-12-22&end_date=2023-03-20&daily=temperature_2m_mean,apparent_temperature_mean,windspeed_10m_max,winddirection_10m_dominant&timezone=America%2FSao_Paulo")

leitura = dados.json()

dados1 = []
dados2 = []

'''
Essa estrutura for percorre a lista de valores que contenham a data diretamente do provedor de webservice.
São criadas as cinco primeiras variáveis baseadas nas informações contidas no provedor
A duas ultimas são chamadas das funções anteriores para categorizar o vento e sua direção nautica.

Quando a função cat_win é chamada, ela verifica se o valor percorrido em ["daily"]["windspeed_10m_max"] satisfaz algum dos valores contidos na função.
Se sim, o próximo passado será chamar a função dir_nautica e fazer a leitura dos valores em ''direcao''
Ela irá percorrer toda lista e condicionar se satisfaz as duas condições da função. Ser maior ou igual aos graus somando e diminuindo o valor de 22.5

'''

l = []
linha = ''
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

    dados1.append(dir_nautica)
    dados2.append(categoria)

c = [(a,b) for a,b in zip(dados1,dados2)]

ultimo = []
montagem_csv = ''
for a,b in c:
    teste = (a,b)
    calculado = c.count(teste)
    listado = [a, calculado, b]
    if listado in ultimo:
        l = 0
    else:
        ultimo.append(listado)
        montagem_csv += f'{a};{calculado};{b}\n'
        arq=open('final.csv', 'w')
        arq.write(montagem_csv)
        arq.close()




