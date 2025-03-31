# Para o próximo passo, vamos transformar os arquivos baixados como PDF
# Que estão com os nomes de anexo_1 e anexo_2, em arquivos zip

# importanto as bibliotecas necessárias para essa transformação
import os
import zipfile

# Vamos criar um arquivos .zip:
"o parâmetro zipfile.ZIP_DEFLATED serve para comprimir os arquivos"
with zipfile.ZipFile("anexos.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    # Verifica os arquivos na pasta anexos
    for arquivo in os.listdir("anexos"):
        # Verifica se os arquivos são .PDF
        if arquivo.endswith(".pdf"):
            # Adiciona os arquivos ao ZIP
            zipf.write(os.path.join("anexos", arquivo), arquivo)

    print("Arquivos compactados com sucesso!")
