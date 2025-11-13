import requests

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()[moeda + 'BRL']
    valor = float(dados['bid'])
    maximo = float(dados['high'])
    minimo = float(dados['low'])
    data = dados['create_date']
    return f"""Moeda: {moeda}/BRL
    Valor: R${valor:.2f}
    Maximo: {maximo:.2f}
    Minimo: {minimo:.2f}
    Atualização: {data}"""

moeda = input("Digite o código da moeda (USD, EUR): ").upper()
print(obter_cotacao(moeda))