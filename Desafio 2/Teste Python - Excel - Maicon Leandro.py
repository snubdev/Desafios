import requests
from bs4 import BeautifulSoup
from datetime import datetime

def getLinks(url, depth, name_arquivo):

    list_liks = []
    links = []

    horario = datetime.now()
    h = f'{horario.hour}:{horario.minute}:{horario.second}'

    page = requests.get(url)
    page_text = page.text
    soup = BeautifulSoup(page_text, 'html.parser')

    for i in soup.find_all('a'):
        links.append(i.get('href'))


    def filtro(links):
        links_2 = []
        for i in range(len(links)):
            try:
                if 'https' in links[i]:
                    links_2.append(links[i])
                elif 'http' in links[i]:
                    links_2.append(links[i])
                else:
                    continue
            except TypeError:
                continue

        link_tot = []

        for element in links_2:
            if element not in link_tot:
                link_tot.append(element)


        return link_tot


    cont = 0
    while True:
        list_liks.append(filtro(links)[cont])
        list_liks.append(h)
        cont += 1
        if cont > depth:
            break

    f = open(name_arquivo, 'w')
    for d in range(len(list_liks)):
        if d % 2 == 0:
            texto = 'link: ' + list_liks[d] + ' -' + ' horario: '+ list_liks[d+1] + '\n'
            print(texto)
            f.write(texto)
    f.close()

    return url, depth, name_arquivo

getLinks('https://enttry.com.br', 2 , 'linksEnttry.csv')








