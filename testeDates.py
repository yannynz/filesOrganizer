import os
import time

# Set the path to the desktop
desktop_path = os.path.expanduser("~/Documentos/testPaste/")

# Create the base filename
base_filename = "file_{}"

# Generate a list of modification dates from 2015 to 2023
modification_dates = [time.strftime("%Y%m%d%H%M%S", time.localtime(time.time() - (365*24*60*60)*(2023-year))) for year in range(2015, 2024)]

# Create up to 10 files with the specified modification dates
for i, date in enumerate(modification_dates):
    if i >= 1:
        break
    filename = base_filename.format(date)
    file_path = os.path.join(desktop_path, filename)
    with open(file_path, 'w') as f:
        f.write("This file was created for testing purposes.")
    
    # Convert the date string to a timestamp
    date_timestamp = time.mktime(time.strptime(date, "%Y%m%d%H%M%S"))
    
    # Set the modification and access times of the file
    os.utime(file_path, (date_timestamp, date_timestamp))
