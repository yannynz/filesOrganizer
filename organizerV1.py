import os
import shutil
from datetime import datetime

# this script will organizate any files from a pre set folder by the creation year 

def organizar_arquivos():
    # Set the path to the desktop
    desktop_path = os.path.expanduser("~\Documenos\testpaste")

    # Create the folders for each year up to the current year
    current_year = datetime.now().year
    for year in range(2015, current_year+1):
        year_folder = os.path.join(desktop_path, f"FACAS{year:02d}")
        os.makedirs(year_folder, exist_ok=True)

    # Set the path to the directory containing the files
    directory_path = os.path.join(desktop_path, "")

    # Loop through all the files in the directory
    for arquivo in os.listdir(directory_path):
        # Get the full path to the file
        file_path = os.path.join(directory_path, arquivo)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Obtain the creation time of the file
        try:
            data_criacao = datetime.fromtimestamp(os.path.getctime(file_path))
        except OSError:
            print(f"Could not get creation time for {arquivo}. Skipping...")
            continue

        # Extract the year of creation
        ano = str(data_criacao.year)

        # Convert the 'ano' variable to an integer
        ano = int(ano)

        # Get the destination directory for the year
        diretorio_destino = os.path.join(desktop_path, f"FACAS{ano:02d}")

        # Move the file to the destination directory
        shutil.move(file_path, os.path.join(diretorio_destino, arquivo))

# Call the function to organize the files
organizar_arquivos()