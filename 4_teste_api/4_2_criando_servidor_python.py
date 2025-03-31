# Importando as bibliotecas para a criação da API
from fastapi import FastAPI, Query
import pandas as pd

# Criando a API
app = FastAPI()

# Carregando os dados do CSV previamente preparado
CSV_PATH = "./3_teste_banco_dados/dados_cadastrais/Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, enconding="latin-1", delimiter=";")

@app.get("/buscar/")
def buscar_operadores(nome: str = Query(..., min_length=3)):
    # Buscando operadores de saúde pelo nome
    resultados = df[df["Nome_Fantasia"].str.contains(nome, case=False, na=False)]

    # Ordenar os resultados por relevância, se necessário, pode-se usar a contagem de ocorrências
    resultados['relevancia'] = resultados["Nome Fantasia"].apply(lambda x: x.lower().count(nome.lower()))
    resultados = resultados.sort_values(by='relevancia', ascending=False)

    # Retornar os resultados como dicionário
    return resultados.to_dict(orient="records")
