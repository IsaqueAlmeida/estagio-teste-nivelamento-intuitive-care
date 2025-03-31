# Importando a biblioteca pandas
import pandas as pd
# Ao primeiro momento, iria fazer a leitura do .pdf com o Pandas
# Contudo, o pandas não faz a leitura de pdf, então, decidi utilizar
# a biblioteca pdfplumber para essa necessidade
import pdfplumber

# Nesse momento, vamos abrir o arquivo pdf utilizando o pdfplumber
# Também iremos fazer o tratamento de erros
tabelas = []
try:
    with pdfplumber.open("../anexos/anexo_1.pdf") as pdf:
        # vamos listar as tabelas para salvar todos os dados
        # Vamos iterar para passar por todos os dados
        for page in pdf.pages:
            tabela = page.extract_tables()
            if tabela:  # Verifica se há uma tabela na página
                # Definindo o cabeçalho
                df = pd.DataFrame(tabela[0][1:], columns=tabela[0][0])
                tabelas.append(df)
    # Vamos juntar todas as tabelas em um único DataFrame
    df_final = pd.concat(tabelas, ignore_index=True)

    # Exibindo o DataFrame completo
    # print(df_final)
    # Após extrair todos os dados do anexo_1,
    # vamos salvar o DataFrame em um CSV
    df_final.to_csv("../anexos_csv/anexo_1.csv", index=False)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
