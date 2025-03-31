# Utilizando o pandas para a renomeação das colunas: OD e AMB
import pandas as pd

# Primeiramente, vamos observar o arquivo csv e verificar as colunas
df = pd.read_csv("../anexos_csv/anexo_1.csv")
# o print servirá para a verificação do DataFrame completo
print(df)

"""Todos esses prints serão comentados para que não atrapalhe
a visualização do DataFrame e até mesmo, na renomeação das colunas.
Foi preciso fazer esses observações com os prints, para ter uma ideia
de como os dados estavam funcionandos, valores nulos,
a descrição e as informações:"""

# Observando só as colunas OD e AMB
# print(df[["OD", "AMB"]])
# # Observando a descrição das colunas
# print(df[["OD", "AMB"]].describe())
# # Antes de fazer a renomeação, vamos verificar os infos sobre as colunas
# print(df[["OD", "AMB"]].info())

# # Verificando se tem valores nulos nas colunas
# print(df.isnull().sum())


# Após uma breve verificação das colunas, das descrições e dos infos,
# vamos renomear as colunas
df.columns = df.columns.str.replace("OD", "Seg. Odontológica")
df.columns = df.columns.str.replace("AMB", "Seg. Ambulatorial")
# Verificando, através do df.columns, se as colunas foram renomeadas
print(df.columns)
