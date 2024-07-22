import os
import time
import random

# Define the path to the directory
directory_path = os.path.expanduser("~/Documentos/testPaste/")

# Define the base filename structure
base_filename = "NR{nr}{cliente}{prioridade}.pdf"

# List of client names
clientes = ["macaco", "aveztruz", "boi", "vaca", "cavalo"]

# List of priorities
prioridades = ["Vermelho", "Amarelo", "Azul", "Verde"]

# Generate a list of modification dates from 2015 to 2023
modification_dates = [time.strftime("%Y%m%d%H%M%S", time.localtime(time.time() - (365*24*60*60)*(2023-year))) for year in range(2015, 2024)]

# Create up to 10 files with the specified modification dates
for i, date in enumerate(modification_dates):
    if i >= 10:
        break
    
    # Generate random nr and select a random client and priority
    nr = random.randint(100000, 999999)
    cliente = random.choice(clientes)
    prioridade = random.choice(prioridades)
    
    # Create the filename with the required pattern
    filename = base_filename.format(nr=nr, cliente=cliente, prioridade=prioridade)
    file_path = os.path.join(directory_path, filename)
    
    # Create and write content to the file
    with open(file_path, 'w') as f:
        f.write(f"This file was created for testing purposes.\nClient: {cliente}\nPriority: {prioridade}")
    
    # Convert the date string to a timestamp
    date_timestamp = time.mktime(time.strptime(date, "%Y%m%d%H%M%S"))
    
    # Set the modification and access times of the file
    os.utime(file_path, (date_timestamp, date_timestamp))

print("Files created successfully.")
