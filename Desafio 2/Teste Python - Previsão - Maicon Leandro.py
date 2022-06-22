# Retornar a temperatura atual de um CEP específico

import requests
from bs4 import BeautifulSoup
import urllib.request, json

n = input("Informe um CEP:")  # Só aceitar Números

def cep_temp (cep):
    try:
        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep}/json/") as url:
            dados = json.loads(url.read().decode())

        cidade = dados['localidade']

        url = 'https://www.google.com/search?q=' + 'weather' + cidade
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        temperatura = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

        print(f'Cidade: {cidade}')
        print(f'Temperatura: {temperatura}º')

    except urllib.error.HTTPError or KeyError:
        print('O CEP INFORMADO NÃO EXISTE')

    return cep

cep_temp(n)

