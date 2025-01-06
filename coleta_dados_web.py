import requests
from bs4 import BeautifulSoup

title_count = 0
paragraf_count = 0
a_count = 0

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Erro ao acessar {url}. Status code: {response.status_code}")
    
def parse_html(html_content):
    
    return BeautifulSoup(html_content, features='html.parser')

def extract_titles(soup, tag='h2'):
    
    global title_count
    titles = []
    for text_line in soup.find_all(tag):
        title = text_line.text.strip()
        titles.append(title)
        title_count += 1
    return titles

def extract_paragraf(soup, tag='p'):
    
    global paragraf_count
    paragrafs = []
    for text_line in soup.find_all(tag):
        paragraf = text_line.text.strip()
        paragrafs.append(paragraf)
        paragraf_count += 1
    return paragrafs

def extract_a(soup, tag='a'):

    global a_count
    tag_a = []
    for text_line in soup.find_all(tag, href=True):
        text_a = text_line.text.strip()
        href = text_line.get("href", "URL não encontrada")
        tag_a.append({"text": text_a, "href": href})
        a_count += 1
    return tag_a

def main():
    
    url = 'https://wiki.python.org.br/AprendaMais'

# 1. Buscar o HTML
    html_content = fetch_html(url)

# 2. Parsear o HTML
    soup = parse_html(html_content)

# 3. Extrair e exibir os títulos
    titles = extract_titles(soup, tag='h2')
    print('Títulos encontrados: ')
    for title in titles:
        print('Título: ', title)

# 4. Extrair e exibir os parágrafos
    paragrafs = extract_paragraf(soup, tag='p')
    print('Parágrafos encontrados: ')
    for prg in paragrafs:
        print('Parágrafo: ', prg)

# 5. Exibir contadores
    print(f'\n Número de títulos encontrados: {title_count}')
    print(f'\n Número de parágrafos encontrados: {paragraf_count}')

# 6. Extrair tags a
    tag_a = extract_a(soup, tag='a')
    print('Tags (a) encontradas: ')
    for a in tag_a:
        text = a["text"]
        href = a["href"]
        print(f'Tag a: {text} | URL: {href}')

# Executa o script
if __name__ == "__main__":
    main()