# Documentação do Script: Coleta de Dados Históricos do Índice Bovespa

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
