import psutil
import hashlib
import csv
from CSV_to_MongoDB import *

import tkinter as tk
import subprocess
from tkinter import filedialog

def get_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def services_hash(parent, x, y, Label):
    services = psutil.win_service_iter()
    
    i = 0

    with open('services_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Service name', 'Executable path', 'SHA256 hash'])
        for service in services:
            try:
                binpath = service.as_dict()['binpath']
                binpath = binpath.split(' ', 1)[0]  # Split the path based on the first space character
                
                if i%300 == 0:
                    pro = "■"
                elif i%12 == 0:
                    pro += "■"
                y.configure(text="status : scanning    "+pro)
                parent.update()
                i+=1

                x.configure(text="scanning : "+str(service))
                parent.update()

                hash_value = get_hash(binpath)
                writer.writerow([service.name(), binpath, hash_value])
            except Exception as e:
                pass
    y.configure(text="status : Done!")
    parent.update()
    x.configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\services_hashes.csv')