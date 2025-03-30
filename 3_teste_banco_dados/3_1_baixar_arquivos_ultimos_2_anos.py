import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

try:
    # Criando a pasta onde os arquivos serão baixados
    dc = "demonstracoes_contabeis"
    os.makedirs(dc, exist_ok=True)

    # URL base do site
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

    # Fazendo a requisição para obter a lista de anos disponíveis
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Determina o ano limite (últimos dois anos)
    ano_limite = datetime.now().year - 2

    # Encontrando os diretórios correspondentes aos anos desejados
    anos_disponiveis = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        # Verifica se o link representa um diretório de ano (ex: "2023/")
        if href[:-1].isdigit():
            ano = int(href[:-1])
            if ano >= ano_limite:
                anos_disponiveis.append(href)

    # Iterar sobre os diretórios de anos disponíveis e baixar os arquivos
    for ano_pasta in anos_disponiveis:
        url_ano = url + ano_pasta
        response_ano = requests.get(url_ano)
        soup_ano = BeautifulSoup(response_ano.text, "html.parser")

        # Criando a pasta do ano correspondente
        pasta_ano = os.path.join(dc, ano_pasta.strip("/"))
        os.makedirs(pasta_ano, exist_ok=True)

        for link in soup_ano.find_all("a", href=True):
            arquivo = link["href"]

            # Garante que seja um arquivo e não um diretório
            if not arquivo.endswith("/"):
                arquivo_url = url_ano + arquivo
                arquivo_nome = os.path.join(pasta_ano, arquivo)

                # Baixando o arquivo
                print(f"Baixando {arquivo}...")
                resposta = requests.get(arquivo_url, stream=True)
                resposta.raise_for_status()

                with open(arquivo_nome, "wb") as f:
                    for chunk in resposta.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"{arquivo} baixado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("Download concluído com sucesso!")
