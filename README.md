
---

# **Projeto de Teste de Estágio - Web Scraping e Transformação de Dados**

Este repositório contém o código para realizar a coleta de arquivos PDF de uma página web, transformá-los em arquivos CSV, compactá-los em formato ZIP e realizar o processamento e renomeação de colunas de um arquivo CSV, além de teste de Banco de Dados e Teste de API.

# 1 - Web Scraping

## **Estrutura do Projeto**



### 1. **Web Scraping**

- **Pasta**: `1_web_scraping`
  - `1_1_web_scraping.py`: Realiza o web scraping para baixar os anexos PDF da página web.
  - `1_3_pdf_zip.py`: Comprime os arquivos PDF baixados em um único arquivo ZIP.
  - `link.py`: Contém os links extraídos da página HTML.

### 2. **Transformação de Dados**

- **Pasta**: `2_transformacao_dados`
  - `2_2_transformacao_dados.py`: Extrai tabelas dos arquivos PDF e salva os dados em arquivos CSV.
  - `2_3_transformacao_csv_em_zip.py`: Comprime os arquivos CSV gerados em um arquivo ZIP.
  - `2_4_substituindo_od_amb.py`: Renomeia as colunas de um arquivo CSV (colunas "OD" e "AMB").

---

## **Passo a Passo**

### **1. Web Scraping - Baixando Arquivos PDF**

No arquivo `1_1_web_scraping.py`, o código realiza o web scraping da seguinte maneira:

1. **Requisição HTTP**: Utiliza a biblioteca `requests` para fazer uma requisição GET para a URL fornecida.
2. **Parsing HTML**: Com a biblioteca `BeautifulSoup`, o código realiza o parsing do HTML da página e encontra os links dos anexos.
3. **Extração dos Links**: Filtra os links que terminam com `.pdf` e são relevantes para o download.
4. **Download dos Arquivos PDF**: Usa a função `requests.get` para baixar os arquivos PDF encontrados.
5. **Salvamento dos Arquivos**: Os arquivos são salvos na pasta `anexos`.

#### **Código:**

```python
import requests
from bs4 import BeautifulSoup
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")

links = []
for link in soup.find_all("a", attrs={"class": "internal-link"}):
    href = link["href"]
    if href.lower().endswith((".pdf", "anexo I", "anexo II")):
        links.append(href)

# Baixando os arquivos
anexo_1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
anexo_2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

# Baixando os arquivos
resposta_1 = requests.get(anexo_1)
resposta_2 = requests.get(anexo_2)

# Criando a pasta e salvando os arquivos
os.makedirs("anexos", exist_ok=True)
if resposta_1.status_code == 200:
    with open("anexos/anexo_1.pdf", "wb") as f:
        f.write(resposta_1.content)
if resposta_2.status_code == 200:
    with open("anexos/anexo_2.pdf", "wb") as f:
        f.write(resposta_2.content)
```

---

### **2. Compactando os Arquivos PDF em ZIP**

No arquivo `1_3_pdf_zip.py`, o código compacta os arquivos PDF baixados em um arquivo ZIP:

1. **Criação do Arquivo ZIP**: Utiliza a biblioteca `zipfile` para criar um arquivo ZIP contendo os PDFs baixados.
2. **Verificação e Adição dos Arquivos**: O código verifica os arquivos na pasta `anexos` e adiciona os PDFs ao arquivo ZIP.

#### **Código:**

```python
import zipfile
import os

with zipfile.ZipFile("anexos.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for arquivo in os.listdir("anexos"):
        if arquivo.endswith(".pdf"):
            zipf.write(os.path.join("anexos", arquivo), arquivo)
```

---
# 2 - Transformação de Dados

### **3. Transformação de Dados - Extração de Tabelas de PDF**

O arquivo `2_2_transformacao_dados.py` realiza a extração de tabelas de arquivos PDF usando a biblioteca `pdfplumber` e salva os dados em formato CSV:

1. **Leitura do PDF**: Abre o arquivo PDF usando `pdfplumber`.
2. **Extração das Tabelas**: Itera sobre as páginas do PDF e extrai as tabelas.
3. **Conversão para CSV**: Usa `pandas` para criar um DataFrame e salvar os dados extraídos em um arquivo CSV.

#### **Código:**

```python
import pandas as pd
import pdfplumber

tabelas = []
try:
    with pdfplumber.open("../anexos/anexo_1.pdf") as pdf:
        for page in pdf.pages:
            tabela = page.extract_tables()
            if tabela:
                df = pd.DataFrame(tabela[0][1:], columns=tabela[0][0])
                tabelas.append(df)
    df_final = pd.concat(tabelas, ignore_index=True)
    df_final.to_csv("../anexos_csv/anexo_1.csv", index=False)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

---

### **4. Compactando os Arquivos CSV em ZIP**

O arquivo `2_3_transformacao_csv_em_zip.py` compacta os arquivos CSV gerados em um arquivo ZIP:

#### **Código:**

```python
import zipfile
import os

renomeando = "Teste_Isaque.zip"
try:
    with zipfile.ZipFile(renomeando, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir("../anexos_csv"):
            if arquivo.endswith(".csv"):
                zipf.write(os.path.join("../anexos_csv", arquivo), arquivo)
    print(f"Arquivo compactado com sucesso com o nome de {renomeando}!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

---

### **5. Renomeação de Colunas em CSV**

O arquivo `2_4_substituindo_od_amb.py` realiza a renomeação das colunas "OD" e "AMB" no arquivo CSV:

1. **Leitura do CSV**: Utiliza `pandas` para carregar o arquivo CSV.
2. **Renomeação das Colunas**: Renomeia as colunas conforme necessário.

#### **Código:**

```python
import pandas as pd

df = pd.read_csv("../anexos_csv/anexo_1.csv")
df.columns = df.columns.str.replace("OD", "Seg. Odontológica")
df.columns = df.columns.str.replace("AMB", "Seg. Ambulatorial")
print(df.columns)
```

---

## **Arquivos Resultantes**

Após a execução de todos os scripts, os seguintes arquivos são gerados:

- **Arquivos PDF**: `anexos/anexo_1.pdf`, `anexos/anexo_2.pdf`
- **Arquivo ZIP com PDFs**: `anexos.zip`
- **Arquivos CSV**: `anexos_csv/anexo_1.csv`
- **Arquivo ZIP com CSVs**: `Teste_Isaque.zip`

---

## **Como Executar o Projeto**

1. **Instalar as dependências**:

   - `requests`
   - `beautifulsoup4`
   - `pandas`
   - `pdfplumber`

   Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install requests beautifulsoup4 pandas pdfplumber
   ```

2. **Executar os Scripts**:

   - Primeiro, execute `1_1_web_scraping.py` para baixar os arquivos PDF.
   - Em seguida, execute `1_3_pdf_zip.py` para compactar os PDFs em um arquivo ZIP.
   - Execute `2_2_transformacao_dados.py` para extrair os dados das tabelas e salvar em CSV.
   - Execute `2_3_transformacao_csv_em_zip.py` para compactar os arquivos CSV.
   - Finalmente, execute `2_4_substituindo_od_amb.py` para renomear as colunas "OD" e "AMB".


---

# 3 - Teste de Banco de Dados

## Estrutura de Pastas 

3_teste_banco_dados/
│
├── dados_cadastrais/
│   └── Relatorio_cadop.csv
│
├── demonstracoes_contabeis/
│   ├── 2023/
│   └── 2024/
│
├── demonstracoes_contabeis_extraidos/
│   ├── 1T2023.csv
│   └── outros arquivos extraídos
│
├── 3_1_baixar_arquivos_ultimos_2_anos.py
├── 3_1_2_transformando_zip_em_csv.py
├── 3_2_baixar_dados_cadastrais.py
├── 3_3_elaborando_queries.sql
├── 3_4_carregar_dados_csv_banco_dados.sql
└── 3_5_querie_analitica.sql


## Descrição dos Arquivos

### 1. **3_1_baixar_arquivos_ultimos_2_anos.py**

Este script realiza o download de arquivos de demonstrações contábeis de dois anos (últimos dois anos) diretamente de uma URL pública.

#### Funcionamento:

- **Bibliotecas Importadas:**
  - `requests`: Para realizar as requisições HTTP.
  - `BeautifulSoup`: Para analisar e extrair dados da página HTML.
  - `datetime`: Para calcular o ano atual e determinar o limite de dois anos atrás.
  - `os`: Para gerenciar pastas e arquivos locais.

- **Etapas:**
  1. Criação de uma pasta `demonstracoes_contabeis` onde os arquivos serão armazenados.
  2. Requisição para obter a lista de diretórios de anos disponíveis.
  3. Filtragem dos anos que são mais recentes do que dois anos atrás.
  4. Para cada ano válido, o script baixa os arquivos contidos no diretório correspondente.

### 2. **3_1_2_transformando_zip_em_csv.py**

Este script descompacta os arquivos `.zip` baixados e os extrai para o formato `.csv`.

#### Funcionamento:

- **Bibliotecas Importadas:**
  - `zipfile`: Para manipulação de arquivos `.zip`.
  - `os`: Para criação de diretórios e gerenciamento de arquivos locais.

- **Etapas:**
  1. Criação de uma pasta `demonstracoes_contabeis_extraidos` para armazenar os arquivos descompactados.
  2. Descompactação de arquivos `.zip` para os diretórios `2023` e `2024`.
  3. Extração de todos os arquivos `.zip` para o diretório de saída.

### 3. **3_2_baixar_dados_cadastrais.py**

Este script realiza o download do arquivo `Relatorio_cadop.csv` com informações cadastrais das operadoras de planos de saúde.

#### Funcionamento:

- **Bibliotecas Importadas:**
  - `requests`: Para realizar a requisição HTTP.
  - `BeautifulSoup`: Para analisar a página HTML e localizar links.

- **Etapas:**
  1. Criação de uma pasta `dados_cadastrais` para armazenar o arquivo baixado.
  2. Requisição para obter os dados do arquivo `Relatorio_cadop.csv`.
  3. Verificação dos links na página e confirmação de que o arquivo `.csv` está disponível.
  4. Download do arquivo e armazenamento local.

### 4. **3_3_elaborando_queries.sql**

Este arquivo contém as instruções SQL para criar as tabelas no banco de dados, conforme os dados dos arquivos `.csv`.

#### Tabelas Criadas:

- **operadoras_saude**: Contém informações sobre as operadoras de planos de saúde.
- **demonstracoes_contabeis**: Contém as demonstrações contábeis das operadoras.

#### Estrutura das Tabelas:

```sql
CREATE TABLE operadoras_saude (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    data_registro DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    competencia VARCHAR(10),
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    receita DECIMAL(15,2),
    despesa DECIMAL(15,2),
    resultado DECIMAL(15,2),
    patrimonio_liquido DECIMAL(15,2)
);
```

### 5. **3_4_carregar_dados_csv_banco_dados.sql**

Este script SQL realiza a carga dos arquivos `.csv` para as tabelas criadas no banco de dados.

#### Carga dos Dados:

- **Dados de Operadoras**: A partir do arquivo `Relatorio_cadop.csv`.
- **Demonstrações Contábeis**: A partir do arquivo `1T2023.csv`.

#### Exemplo de Carga:

```sql
COPY operadoras_saude(
  registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
  logradouro, numero, complemento, bairro, cidade, uf, cep,
  ddd, telefone, fax, endereco_eletronico, representante,
  cargo_representante, data_registro
) FROM './dados_cadastrais/Relatorio_cadop.csv'
DELIMITER ";"
CSV HEADER;

COPY demonstracoes_contabeis(
  competencia, registro_ans, cnpj, receita, despesa, resultado,
  patrimonio_liquido
) FROM './demonstracoes_contabeis_extraidos/1T2023.csv'
DELIMITER ";"
CSV HEADER;
```

### 6. **3_5_querie_analitica.sql**

Este arquivo contém consultas SQL para análise dos dados, realizando agregações e visualizações importantes.

#### Exemplos de Consultas:

1. **Total de Operadoras por Estado:**

   ```sql
   SELECT uf, COUNT(*) AS total_operadoras 
   FROM operadoras_saude 
   GROUP BY uf 
   ORDER BY total_operadoras DESC;
   ```

2. **Receita Total por Operadora:**

   ```sql
   SELECT o.nome_fantasia, SUM(d.receita) AS receita_total 
   FROM demonstracoes_contabeis d
   JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
   GROUP BY o.nome_fantasia 
   ORDER BY receita_total DESC;
   ```

3. **Demonstrativo Financeiro por Operadora:**

   ```sql
   SELECT o.nome_fantasia, d.competencia, d.receita, d.despesa, d.resultado, d.patrimonio_liquido 
   FROM demonstracoes_contabeis d
   JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
   ORDER BY o.nome_fantasia, d.competencia;
   ```

4. **Top 10 Operadoras com Maiores Despesas no Último Trimestre:**

   ```sql
   SELECT o.nome_fantasia, d.competencia, d.despesa 
   FROM demonstracoes_contabeis d
   JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
   WHERE d.competencia IN ('4T2024', '3T2024', '2T2024') 
   ORDER BY d.despesa DESC 
   LIMIT 10;
   ```

5. **Top 10 Operadoras com Maiores Despesas no Último Ano:**

   ```sql
   SELECT o.nome_fantasia, SUM(d.despesa) AS total_despesa 
   FROM demonstracoes_contabeis d
   JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
   WHERE d.competencia LIKE '%2024' 
   GROUP BY o.nome_fantasia 
   ORDER BY total_despesa DESC 
   LIMIT 10;
   ```

## Como Usar

1. **Baixar os Arquivos:**
   - Execute os scripts `3_1_baixar_arquivos_ultimos_2_anos.py` e `3_2_baixar_dados_cadastrais.py` para baixar os arquivos necessários.

2. **Descompactar os Arquivos:**
   - Execute o script `3_1_2_transformando_zip_em_csv.py` para descompactar os arquivos `.zip` para o formato `.csv`.

3. **Carregar os Dados no Banco:**
   - Utilize os scripts SQL `3_3_elaborando_queries.sql`, `3_4_carregar_dados_csv_banco_dados.sql` e `3_5_querie_analitica.sql` para criar as tabelas, carregar os dados e realizar análises.

Aqui está a continuação do README.md detalhado para a pasta `4_teste_api`, com as explicações sobre os códigos contidos nela. O objetivo é fornecer um guia completo, claro e bem estruturado para o RH, com a explicação do código da API criada em Python e do arquivo de coleção do Postman.

---
# 4 - Teste de API

## Estrutura de Pastas

```
4_teste_api/
│
├── 4_2_criando_servidor_python.py
├── colecao_postman.json
```

## Descrição dos Arquivos

### 1. **4_2_criando_servidor_python.py**

Este script cria uma API RESTful usando o framework `FastAPI` para expor um serviço que permite buscar informações sobre operadoras de planos de saúde a partir de um arquivo `.csv`.

#### Funcionamento:

- **Bibliotecas Importadas:**
  - `fastapi.FastAPI`: Para a criação da API.
  - `fastapi.Query`: Para fazer uso de parâmetros de consulta na URL da API.
  - `pandas`: Para manipulação e leitura de dados dos arquivos `.csv`.

- **Passos do Código:**
  1. **Criação da API:**
     - A instância `app` é criada a partir da classe `FastAPI`.
  
  2. **Leitura do Arquivo CSV:**
     - O arquivo `Relatorio_cadop.csv` é carregado para um DataFrame do Pandas, que contém informações sobre operadoras de saúde. 
     - O caminho do arquivo é especificado em `CSV_PATH`.
     - O arquivo é lido usando o `pandas.read_csv()` com o encoding "latin-1" e delimitador `;`.

  3. **Criação do Endpoint `/buscar/`:**
     - O endpoint é definido como um método `GET` utilizando o decorador `@app.get("/buscar/")`.
     - O parâmetro `nome` é obrigatório e deve ter pelo menos 3 caracteres. Esse parâmetro é usado para buscar operadoras que possuem o nome (ou parte dele) informado.
  
  4. **Lógica de Busca:**
     - A busca é realizada no DataFrame `df`, onde se verifica se o campo `Nome_Fantasia` contém o texto fornecido no parâmetro `nome` (ignorando maiúsculas/minúsculas).
     - O campo `relevancia` é calculado pela contagem de ocorrências do nome fornecido em cada `Nome_Fantasia`.
     - O DataFrame resultante é ordenado pela relevância da busca (em ordem decrescente).
  
  5. **Retorno dos Resultados:**
     - O resultado é retornado como um dicionário, com a estrutura `orient="records"`, onde cada linha do DataFrame é convertida em um registro JSON.

#### Código:

```python
from fastapi import FastAPI, Query
import pandas as pd

# Criando a API
app = FastAPI()

# Carregando os dados do CSV previamente preparado
CSV_PATH = "./3_teste_banco_dados/dados_cadastrais/Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, encoding="latin-1", delimiter=";")

@app.get("/buscar/")
def buscar_operadores(nome: str = Query(..., min_length=3)):
    # Buscando operadores de saúde pelo nome
    resultados = df[df["Nome_Fantasia"].str.contains(nome, case=False, na=False)]

    # Ordenar os resultados por relevância, se necessário, pode-se usar a contagem de ocorrências
    resultados['relevancia'] = resultados["Nome Fantasia"].apply(lambda x: x.lower().count(nome.lower()))
    resultados = resultados.sort_values(by='relevancia', ascending=False)

    # Retornar os resultados como dicionário
    return resultados.to_dict(orient="records")
```

### 2. **colecao_postman.json**

Este arquivo contém a coleção do Postman usada para testar a API criada no script Python. Ele define a requisição para o endpoint `/buscar/` e um exemplo de resposta.

#### Estrutura do Arquivo JSON:

- **info**: Contém informações gerais sobre a coleção do Postman.
  - `name`: Nome da coleção ("Operadoras API").
  - `schema`: Esquema de versão do Postman.

- **item**: Define os detalhes da requisição HTTP.
  - **name**: Nome da requisição ("Buscar Operadoras").
  - **request**: Detalhes sobre o método HTTP (`GET`), a URL e o parâmetro de consulta `nome`.
    - A URL da requisição é construída com base na variável `base_url`, que está configurada para o valor `http://127.0.0.1:5000`.
    - O parâmetro `nome` na URL está configurado para buscar a operadora "UNIMED", mas pode ser substituído conforme necessário.

- **response**: Contém um exemplo de resposta para a requisição, com um código de status HTTP 200 e um corpo JSON que representa duas operadoras com o nome "UNIMED".

#### Exemplo de Requisição e Resposta:

```json
{
  "info": {
    "_postman_id": "your-postman-id",
    "name": "Operadoras API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Buscar Operadoras",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/buscar-operadoras?nome=UNIMED",
          "host": ["{{base_url}}"],
          "path": ["buscar-operadoras"],
          "query": [
            {
              "key": "nome",
              "value": "UNIMED",
              "description": "Nome da operadora a ser buscada"
            }
          ]
        }
      },
      "response": [
        {
          "name": "Exemplo de resposta",
          "status": "200 OK",
          "code": 200,
          "body": "{\n  \"operadoras\": [\n    {\n      \"id\": 1,\n      \"nome\": \"UNIMED SP\",\n      \"registro_ans\": \"12345\",\n      \"cnpj\": \"00.000.000/0001-00\"\n    },\n    {\n      \"id\": 2,\n      \"nome\": \"UNIMED RJ\",\n      \"registro_ans\": \"67890\",\n      \"cnpj\": \"00.000.000/0002-00\"\n    }\n  ]\n}",
          "header": []
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://127.0.0.1:5000",
      "type": "string"
    }
  ]
}
```
#### Como Usar:

1. **Executar a API:**
   - Execute o script Python `4_2_criando_servidor_python.py` para iniciar o servidor FastAPI localmente. O servidor será iniciado em `http://127.0.0.1:5000`.

2. **Testar a API com o Postman:**
   - Importe o arquivo `colecao_postman.json` no Postman.
   - A requisição configurada no Postman fará uma busca pela operadora "UNIMED".
   - Você pode modificar o parâmetro `nome` para buscar outras operadoras.

3. **Consultar os Resultados:**
   - Ao fazer uma requisição `GET` para `http://127.0.0.1:5000/buscar/`, você obterá um JSON contendo as operadoras que correspondem ao nome fornecido.
---


