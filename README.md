# Documentação do Script

# Coleta de Dados Históricos do Índice Bovespa

Descrição
Este script tem como objetivo acessar a página de dados históricos do índice Bovespa no site Investing.com, realizar o scraping do conteúdo HTML, e, utilizando as bibliotecas BeautifulSoup e pandas, extrair e exibir as tabelas disponíveis na página.

Dependências
Este script utiliza as seguintes bibliotecas Python:

requests: Para fazer a requisição HTTP à URL fornecida.

BeautifulSoup (da biblioteca bs4): Para processar e estruturar o HTML da página.

pandas: Para localizar e manipular tabelas disponíveis no HTML.

Certifique-se de instalá-las antes de executar o script: "pip install requests beautifulsoup4 pandas", no meu caso, foi necessário utilizar o comando "pip3 install..."

Funcionamento do Script:

Requisição HTTP
Utiliza a biblioteca requests para enviar uma requisição GET para a URL do Investing.com.
A resposta contém o HTML bruto da página.

Processamento HTML com BeautifulSoup
O conteúdo HTML da resposta é processado utilizando BeautifulSoup para permitir a formatação e inspeção da estrutura HTML.

Extração de Tabelas com pandas
O script utiliza o método pd.read_html para localizar e extrair todas as tabelas presentes no HTML retornado.
O número de tabelas encontradas e os primeiros 20 registros da primeira tabela são exibidos.

Tratamento de Erros
Caso a função pd.read_html não consiga localizar tabelas ou processar o conteúdo, o erro será capturado e uma mensagem será exibida.

Entradas
Este script não exige entradas do usuário diretamente. A URL da página é definida no código como: "url = 'https://br.investing.com/indices/bovespa-historical-data'"

# HTML Scraper

Este script realiza o scraping de páginas HTML para extrair informações específicas como títulos, parágrafos e links. Ele utiliza as bibliotecas requests e BeautifulSoup para buscar e processar o conteúdo de uma página da web.

Funcionalidades:

Extrai títulos da página (tags '(h2)').
Extrai parágrafos da página (tags '(p)').
Extrai links da página (tags '(a)'com o atributo href).
Conta e exibe o número de títulos, parágrafos e links encontrados.

Arquitetura do Código

1. Funções:
fetch_html(url): Faz a requisição à URL fornecida e retorna o HTML da página.

parse_html(html_content): Converte o HTML bruto em um objeto BeautifulSoup para facilitar a extração.

extract_titles(soup, tag): Extrai títulos da página com base na tag especificada (padrão: '(h2)').

extract_paragraf(soup, tag): Extrai parágrafos da página com base na tag especificada (padrão: '(p)').

extract_a(soup, tag): Extrai links da página com base na tag especificada (padrão: '(a)'), incluindo texto e URLs.

2. Função Principal:
A função main() organiza o fluxo do script:

Faz o download do HTML da página.
Processa o HTML.

Extrai títulos, parágrafos e links.

Exibe os resultados no console.

Notas
O URL da página a ser analisada está configurado como: url = 'https://wiki.python.org.br/AprendaMais'

Você pode alterá-lo para processar outras páginas.

Certifique-se de que a página a ser analisada permite scraping e respeite os termos de uso do site.

# File Upload and Download Script

Este script permite realizar upload e download de arquivos em um serviço de hospedagem de arquivos. Ele também suporta uploads autenticados utilizando uma chave de API.

Pré-requisitos
Certifique-se de que as dependências estão instaladas: 'pip install requests'

Funcionalidades

Upload de Arquivo (Público):
Faz upload de um arquivo para o serviço file.io sem autenticação.

Upload de Arquivo com Chave de API:
Permite o envio autenticado de arquivos utilizando uma chave de API.

Download de Arquivo:
Faz download de um arquivo a partir de uma URL e salva-o localmente.

Arquitetura do Código

Funções
upload_file():
  Faz upload de um arquivo para o serviço file.io sem autenticação.
  Exibe os detalhes da resposta, incluindo o link para o arquivo enviado.
  
download_file(file_url, output_file='arquivo_baixado.xlsx'):
  Faz download de um arquivo a partir de uma URL e o salva localmente com o nome especificado.

upload_file_key():
  Faz upload de um arquivo para o serviço file.io utilizando autenticação via chave de API.
  Exibe os detalhes da resposta, incluindo o link para o arquivo enviado.

Notas

Certifique-se de que a URL do serviço de upload está correta: url='https://file.io/'

O script está configurado para enviar arquivos públicos por padrão. Para maior segurança, use a função upload_file_key() com uma chave de API.
