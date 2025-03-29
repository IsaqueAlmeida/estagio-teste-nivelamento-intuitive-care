# Importando a biblioteca requests para as requisições HTTP
import requests
# Antes de importamos a biblioteca BeautifulSoup, precisamos instalá-la
# - pip install beautifulsoup4
# Importando a biblioteca BeautifulSoup para o parsing do HTML
from bs4 import BeautifulSoup

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
soup.find_all("a", attrs={"class": "internal-link"})

# Após encontrar todos os tags <a> com a class 'internal-link',
# vamos copiar todo esse links e colocar em uma variável
links = (
    """<a class="internal-link"
    data-mce-href="resolveuid/f710899c6c7a485ea62a1acc75d86c8c" """
    """data-mce-style="" """
    """data-tippreview-enabled="true" """
    """data-tippreview-image="" """
    """data-tippreview-title=""
    href="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    """
    """style="" target="_blank" title="">Anexo I.</a>, """
    """<a class="internal-link"
    data-mce-href="resolveuid/aee04d07eec1412e8121f50c277d72b9" """
    """data-mce-style="" """
    """data-tippreview-enabled="true" """
    """data-tippreview-image="" """
    """data-tippreview-title=""
    href="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx"""
    """style="" target="_blank" title="">(Anexo I</a>, """
    """<a class="internal-link"
    data-mce-href="resolveuid/85adaa3de5464d8aadea11456bfb4f94" """
    """data-mce-style="" """
    """data-tippreview-enabled="true" """
    """data-tippreview-image="" """
    """data-tippreview-title=""
    href="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"""
    """style="" target="_blank" title="">Anexo II.</a>, """
    """<a class="internal-link" """
    """data-mce-href="resolveuid/26bf4441cb3d4b48a26f59185e90f953" """
    """data-tippreview-enabled="false" data-tippreview-image="" """
    """data-tippreview-title=""
    href="https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/nota13_geas_ggras_dipro_17012013.pdf"""
    """target="_blank" title="">Nota sobre Terminologias</a>, """
    """<a class="internal-link" """
    """data-mce-href="resolveuid/036c5ac8cbd34b859de38c69914d9141" """
    """data-mce-style="" """
    """data-tippreview-enabled="true" """
    """data-tippreview-image="" """
    """data-tippreview-title=""
    href="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/CorrelaoTUSS.202409Rol.2021_TUSS202501_RN627L.2025.xlsx"""
    """style="" target="_blank" title="">Correlação TUSS x Rol </a>"""
)

# Agora que tenho as tags <a> com a class 'internal-link',
# Vamos extrais todas as URLS encontradas na tags <a> da página
soup = BeautifulSoup(links, "html.parser")
# soup.find_all("a", attrs={"class": "internal-link"})
link = []
for links in soup.find_all("a", attrs={"class": "internal-link"}):
    href = links["href"]
    # irá verificar se os links terminam com .PDF
    if href.lower().endswith(".pdf"):
        print(href)
    # else:
    #     print("links não está em PDF")
