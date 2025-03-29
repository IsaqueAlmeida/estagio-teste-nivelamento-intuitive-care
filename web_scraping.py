# Importando a biblioteca requests para as requisições HTTP
import requests
# Antes de importamos a biblioteca BeautifulSoup, precisamos instalá-la
# - pip install beautifulsoup4
# Importando a biblioteca BeautifulSoup para o parsing do HTML
from bs4 import BeautifulSoup
# Importando a biblioteca OS para criar a pasta onde será salvo os arquivos
import os
from link import links

# Logo após as impostações das bibliotecas beautifulsoup4 e requests, vamos
# utilizar a URL passado no PDF do teste técnico
url = (
  "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/"
  "atualizacao-do-rol-de-procedimentos"
)

# Verificando o site para saber as tags e class que os arquivos de anexo I e
# II estão, utilizando o Mozilla Firefox, clicando com o botão direito do mouse
# e clicando em inspecionar, ou apertando F12.
# Verificando a tag <a> e a class 'internal-link,
# onde se encontra os dois anexos
# Após isso, vamos fazer a requisição para o site e o parsing do HTML:

r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")
# print(soup)
# Agora que temos o HTML do site, vamos procurar as tags <a> e a class
# 'internal-link'
link = soup.find_all("a", attrs={"class": "internal-link"})

# Agora que tenho as tags <a> com a class 'internal-link',
# Vamos extrais todas as URLS encontradas na tags <a> da página
soup = BeautifulSoup(links, "html.parser")
# soup.find_all("a", attrs={"class": "internal-link"})
links = []
for links in soup.find_all("a", attrs={"class": "internal-link"}):
    href = links["href"]
    # irá verificar se os links terminam com .PDF
    if href.lower().endswith((".pdf", "anexo I", "anexo II")):
        print(href)
        # link.append(href)

# Após encontrar todos os links que contenha .pdf, que servirá para baixar
# os arquivos, vamos criar um algoritmo para baixar esses arquivos .pdf
# Vamos salvar o link do arquivo .pdf em uma variável e baixar o arquivo
anexo_1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
anexo_2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

resposta_1 = requests.get(anexo_1)
resposta_2 = requests.get(anexo_2)

# Criando a pasta para salvar os arquivos
os.makedirs("anexos", exist_ok=True)

# Após criar a pasta, vamos baixar os arquivos:
# Primeiro vamos baixar o Anexo I
resposta_1 = requests.get(anexo_1)
if resposta_1.status_code == 200:
    with open("anexos/anexo_1.pdf", "wb") as f:
        f.write(resposta_1.content)
    print("Download concluído do anexo_1!")
else:
    print(f"Falha no download! status_code: {resposta_1.status_code}")

# Agora vamos baixar o anexo II
resposta_2 = requests.get(anexo_2)
if resposta_1.status_code == 200:
    with open("anexos/anexo_2.pdf", "wb") as f:
        f.write(resposta_2.content)
    print("Download concluído do arquivo anexo_2!")
else:
    print(f"Falha no download! status_code: {resposta_2.status_code}")
