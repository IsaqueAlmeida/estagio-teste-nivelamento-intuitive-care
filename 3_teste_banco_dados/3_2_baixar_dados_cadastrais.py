# IMportando as bibliotecas necessárias para a requisição
import requests
from bs4 import BeautifulSoup
import os

# Criando a pasta onde o arquivo será baixado
dc = "dados_cadastrais"
os.makedirs(dc, exist_ok=True)

# Verificando a URL
url = (
  "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
)

# Fazendo a requisição
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Verificando a tag a o href
tag = soup.find_all("a", href=True)

# Iterando sobre a tag
for link in soup.find_all("a", href=True):
    href = link["href"]
    # irá verifica se os links terminam com .csv
    if href.lower().endswith(".csv"):
        # A resposta será Relatorio_cadop.csv
        print(href)
        link.append(href)

# Baixando o arquivo Relatorio_cadop.csv
cadastros = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
cadastros = requests.get(cadastros)
if cadastros.status_code == 200:
    with open(os.path.join(dc, "Relatorio_cadop.csv"), "wb") as f:
        f.write(cadastros.content)
    print("Download concluido com sucesso!")
else:
    print("Falha no download!")
