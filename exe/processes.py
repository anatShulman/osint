import csv
import hashlib
import psutil
from CSV_to_MongoDB import *

from getmac import get_mac_address as gma
import getpass
import datetime

import tkinter as tk
import subprocess
from tkinter import filedialog

def processes_hash(parent, lst_labels, collection, Label):
    # Create a list to store the process information
    process_list = []

    i = 0

    # Additional data
    MAC_address = gma()
    user = getpass.getuser()

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
                lst_labels[1].configure(text="status : scanning    "+pro)
                parent.update()
                i+=1

                lst_labels[0].configure(text="scanning : "+str(proc))
                parent.update()
                with open(exe_path, 'rb') as f:
                    sha256_hash = hashlib.sha256(f.read()).hexdigest()
        except (psutil.AccessDenied, FileNotFoundError):
            sha256_hash = 'N/A'

        # Add the process information to the list
        time_now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        process_list.append([proc.info['name'], proc.info['pid'], sha256_hash, parent.username, MAC_address, user, time_now])

        # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
        if lst_labels[2] != 'DB status :       connection failed' and collection != False:
            dict_hash = {'Hash':sha256_hash, 'PID':proc.info['pid'], 'Process name':proc.info['name'], 'email':parent.username, 'MAC':MAC_address, 'user':user, 'time scanned':time_now}
            thread = threading.Thread(target=upload_dict, args=(dict_hash, lst_labels[2], lst_labels[3], parent, collection))
            thread.start()


    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # Write the process information to a CSV file
    with open('process_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'PID', 'Hash', 'Email', 'MAC', 'user', 'time'])
        writer.writerows(process_list)

    # upload(os.getcwd()+'\process_hashes.csv')