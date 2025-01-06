import requests
from bs4 import BeautifulSoup
import pandas as pd


url =  'https://br.investing.com/indices/bovespa-historical-data'

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
#}

print('\nRequest: ')
response = requests.get(url)
print(response.text[:600])

print('\nBeatifulSoup: ')
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:2000])

print('\nPandas: ')
try:
    tables = pd.read_html(response.text)
    print('Número de tabelas encontradas: ', len(tables))

    if tables:
        print(tables[0].head(20))
    else:
        print('Nenhuma tabela encontrada na página')

except ValueError as v:
    print('Erro ao tentar ler tabelas: '. v)