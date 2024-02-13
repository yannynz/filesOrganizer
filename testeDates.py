import os
import time
import win32file
import pywintypes

# Set the path to the desktop
desktop_path = os.path.expanduser("~\Desktop\Teste")

# Create the base filename
base_filename = "file_{}"

# Generate a list of modification dates from 2015 to 2023
modification_dates = [time.strftime("%Y%m%d%H%M%S", time.localtime(time.time() - (365*24*60*60)*(2023-year))) for year in range(2015, 2024)]

# Create up to 25 files with the specified modification dates
for i, date in enumerate(modification_dates):
    if i >= 25:
        break
    filename = base_filename.format(date)
    file_path = os.path.join(desktop_path, filename)
    with open(file_path, 'w') as f:
        f.write("This file was created for testing purposes.")
    # Convert the date string to a Windows FILETIME object
    date_int = int(time.mktime(time.strptime(date, "%Y%m%d%H%M%S")))
    filetime_mod = pywintypes.Time(date_int)
    filetime_creation = filetime_mod
    # Open the file handle
    file_handle = win32file.CreateFile(
        file_path,
        win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ,
        None,
        win32file.OPEN_EXISTING,
        0,
        None
    )
    try:
        # Set the creation and modification times of the file
        win32file.SetFileTime(file_handle, filetime_creation, filetime_mod, filetime_mod)
    finally:
        win32file.CloseHandle(file_handle)