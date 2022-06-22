# Retornar as Meta tags de uma página

import json

from bs4 import BeautifulSoup
import requests

url = 'https://enttry.com.br/contato'
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
page_meta = soup.find_all('meta')
tweetArr = []
for dados in page_meta:
    try:
        tweetObject = {
            'name': dados['name'],
            'content': dados['content'],
        }
    except KeyError:
        continue

    tweetArr.append(tweetObject)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)