import requests

def upload_file():
    
    arq = '/Users/victorhugopradateixeira/Documents/Python(Dados)/produtos_informatica.xlsx'

    try:

        with open(arq, 'rb') as file:
            req = requests.post(url='https://file.io/', files={'file': file})

        print("\nStatus Code:", req.status_code,"\n")
        print("\nResponse Headers:", req.headers,"\n")
        print("\nResponse Text (partial):", req.text[:500],"\n")

        if req.status_code == 200:
            try:
                exit_req = req.json()
                print(exit_req)
                url = exit_req.get('link', 'Link não encontrado')
                dt_expires = exit_req.get('expires', 'Data de expiração não encontrada')
                print(f"\nArquivo enviado, link para acesso em: {url} \nExpira em: {dt_expires}")
            except ValueError:
                print("Erro ao processar resposta JSON.")
        else:
            print(f"Erro na requisição: {req.status_code}")
            print(f"Resposta: {req.text}")
    except FileNotFoundError:
        print("O arquivo não foi encontrado, verifique o caminho.")

def download_file(file_url, output_file='arquivo_baixado.xlsx'):

    try:

        req = requests.get(file_url, timeout=60)
        req.raise_for_status()

        if req.ok:
            with open(output_file, 'wb') as file:
                file.write(req.content)
            print(f"Arquivo baixado com sucesso. {output_file}")
        else:
            print("Erro ao baixar o arquivo")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")
        
def upload_file_key():

    arq = '/Users/victorhugopradateixeira/Documents/Python(Dados)/produtos_informatica.xlsx'
    api_key = 'UUBNRPA.NC2ZAHB-Y66MQDZ-Q00HQK8-WHHM98F'

    try:

        with open(arq, 'rb') as file:
            req = requests.post(
                url='https://file.io/',
                files={'file': file},
                headers={'Authorization': api_key}
            )
        
        print("\nStatus Code:", req.status_code,"\n")
        print("\nResponse Headers:", req.headers,"\n")
        print("\nResponse Text (partial):", req.text[:500],"\n")

        if req.status_code == 200:
            try:
                exit_req = req.json()
                print(exit_req)
                url = exit_req.get('link', 'Link não encontrado')
                dt_expires = exit_req.get('expires', 'Data de expiração não encontrada')
                print(f"\nArquivo enviado com chave de acesso, link para acesso em: {url} \nExpira em: {dt_expires}")
            except ValueError:
                print("Erro ao processar resposta JSON.")
        else:
            print(f"Erro na requisição: {req.status_code}")
            print(f"Resposta: {req.text}")
    except FileNotFoundError:
        print("O arquivo não foi encontrado, verifique o caminho.")






#upload_file()
#download_file('https://file.io/wQvCnykuJ0Yt')
#upload_file_key()