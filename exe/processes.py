import csv
import hashlib
import psutil
from CSV_to_MongoDB import *

def processes_hash():
    # Create a list to store the process information
    process_list = []

    # Iterate over all running processes
    for proc in psutil.process_iter(['name', 'exe', 'pid']):

        # Calculate the SHA256 hash of the process executable file
        try:
            exe_path = proc.info['exe']
            if exe_path is None:
                sha256_hash = 'N/A'
            else:
                with open(exe_path, 'rb') as f:
                    sha256_hash = hashlib.sha256(f.read()).hexdigest()
        except (psutil.AccessDenied, FileNotFoundError):
            sha256_hash = 'N/A'

        # Add the process information to the list
        process_list.append([proc.info['name'], proc.info['pid'], sha256_hash])

    # Write the process information to a CSV file
    with open('process_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'PID', 'Hash'])
        writer.writerows(process_list)

    upload(os.getcwd()+'\process_hashes.csv')