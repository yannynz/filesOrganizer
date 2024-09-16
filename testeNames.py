import os
import time
import random
import string

# Define the path to the directory
directory_path = os.path.expanduser("~/Documentos/testPaste/")

# Define the base filename structure
base_filename = "NR{nr}{cliente}{prioridade}.pdf"

# List of priorities
prioridades = ["Vermelho", "Amarelo", "Azul", "Verde"]

# Generate a list of modification dates from 2015 to 2023
modification_dates = [time.strftime("%Y%m%d%H%M%S", time.localtime(time.time() - (365*24*60*60)*(2023-year))) for year in range(2015, 2024)]
    
# Function to generate a random string of letters
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Create up to 10 files with the specified modification dates
for i, date in enumerate(modification_dates):
    if i >= 1:
        break
    
    # Generate random nr and select a random client and priority
    nr = random.randint(100000, 999999)
    cliente_length = random.randint(5, 10)  # Random length between 5 and 10
    cliente = random_string(cliente_length)
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
