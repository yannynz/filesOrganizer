import os
import shutil
import time

# Define os caminhos para os diretórios de origem e destino
source_directory = os.path.expanduser("~/Documentos/testPaste/")
destination_directory = os.path.expanduser("~/Documentos/FACAS_OK/")

# Função para encontrar o último arquivo modificado no diretório source_directory
def find_latest_file(directory):
    files = os.listdir(directory)  # Lista todos os arquivos no diretório
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]  # Filtra apenas arquivos

    if not files:
        print("Nenhum arquivo encontrado.")
        return None

    # Encontra o arquivo com a data de modificação mais recente
    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    return latest_file

# Mover o último arquivo modificado para o diretório de destino
def move_latest_file():
    latest_file = find_latest_file(source_directory)
    
    if latest_file:
        source_file_path = os.path.join(source_directory, latest_file)
        destination_file_path = os.path.join(destination_directory, latest_file)

        # Move o arquivo para o diretório de destino
        shutil.move(source_file_path, destination_file_path)
        print(f"Arquivo {latest_file} movido para {destination_directory}")
    else:
        print("Nenhum arquivo para mover.")

# Verifica se o diretório de destino existe, se não, cria o diretório
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Executa a função para mover o arquivo
move_latest_file()

