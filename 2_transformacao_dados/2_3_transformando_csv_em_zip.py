# Importando as bilbiotecas para a transformação do arquivo csv em zip
import zipfile
import os

# Vamos utilizar o ZIP_DEFLATED para comprimir o arquivo
# Renomeando o arquivo para Teste_Isaque.zip
renomeando = "Teste_Isaque.zip"
try:
    with zipfile.ZipFile(renomeando, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Verificando os arquivos na pasta anexos_csv
        for arquivo in os.listdir("../anexos_csv"):
            # Verificando se os arquivos são .csv
            if arquivo.endswith(".csv"):
                # Adicionando os arquivos ao ZIP
                zipf.write(os.path.join("../anexos_csv", arquivo), arquivo)
        print(f"Arquivo compactado com sucesso com o nome de {renomeando}!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
