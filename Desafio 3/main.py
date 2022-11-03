import csv

with open(file='exemplo.txt', mode='r', encoding='utf8') as arquivo:
    dados = arquivo.read()
    list_dados = dados.split()

print(list_dados)

with open(file='dado.csv', mode='w', encoding='utf8') as arquivo_novo:
    dados_csv = csv.writer(arquivo_novo)
    dados_csv.writerow(list(map(lambda dado: [dado], list_dados)))



