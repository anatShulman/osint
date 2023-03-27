import csv
import hashlib
import psutil
from CSV_to_MongoDB import *

import tkinter as tk
import subprocess
from tkinter import filedialog

def processes_hash(parent, x, y, Label):
    # Create a list to store the process information
    process_list = []

    i = 0

    # Iterate over all running processes
    for proc in psutil.process_iter(['name', 'exe', 'pid']):

        # Calculate the SHA256 hash of the process executable file
        try:
            exe_path = proc.info['exe']
            if exe_path is None:
                sha256_hash = 'N/A'
            else:
                if i%300 == 0:
                    pro = "■"
                elif i%12 == 0:
                    pro += "■"
                y.configure(text="status : scanning    "+pro)
                parent.update()
                i+=1

                x.configure(text="scanning : "+str(proc))
                parent.update()
                with open(exe_path, 'rb') as f:
                    sha256_hash = hashlib.sha256(f.read()).hexdigest()
        except (psutil.AccessDenied, FileNotFoundError):
            sha256_hash = 'N/A'

        # Add the process information to the list
        process_list.append([proc.info['name'], proc.info['pid'], sha256_hash])
    y.configure(text="status : Done!")
    parent.update()
    x.configure(text="scanning : None")
    parent.update()

    # Write the process information to a CSV file
    with open('process_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'PID', 'Hash'])
        writer.writerows(process_list)

    # upload(os.getcwd()+'\process_hashes.csv')