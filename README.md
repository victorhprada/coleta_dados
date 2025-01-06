# Documentação do Script: Coleta de Dados Históricos do Índice Bovespa

Descrição
Este script tem como objetivo acessar a página de dados históricos do índice Bovespa no site Investing.com, realizar o scraping do conteúdo HTML, e, utilizando as bibliotecas BeautifulSoup e pandas, extrair e exibir as tabelas disponíveis na página.

Dependências
Este script utiliza as seguintes bibliotecas Python:

requests: Para fazer a requisição HTTP à URL fornecida.
BeautifulSoup (da biblioteca bs4): Para processar e estruturar o HTML da página.
pandas: Para localizar e manipular tabelas disponíveis no HTML.
