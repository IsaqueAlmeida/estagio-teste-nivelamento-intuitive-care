import zipfile
import os

# DIretório com os ZIPs
zip_dir_2023 = "./demonstracoes_contabeis/2023/"
zip_dir_2024 = "./demonstracoes_contabeis/2024/"
extract_dir = "demonstracoes_contabeis_extraidos"

# criando pasta para os arquivos extraídos
os.makedirs(extract_dir, exist_ok=True)

# Descompactando todos os ZIPs - 2023
try:
    for zip_file in os.listdir(zip_dir_2023):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(zip_dir_2023, zip_file)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)
            print(f"Descompactado: {zip_file}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Descompactando todos os ZIPs - 2024
try:
    for zip_file in os.listdir(zip_dir_2024):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(zip_dir_2024, zip_file)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)
            print(f"Descompactado: {zip_file}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("Descompactação concluida com sucesso!")
