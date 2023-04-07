import psutil
import hashlib
import csv
from CSV_to_MongoDB import *

from getmac import get_mac_address as gma
import getpass
import datetime
import win32api
import win32con
import win32security

import tkinter as tk
import subprocess
from tkinter import filedialog

import threading

def get_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def services_hash(parent, lst_labels, collection, Label):
    services = psutil.win_service_iter()
    
    i = 0

    # Additional data
    MAC_address = gma()
    user = getpass.getuser()

    with open('services_hashes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Service name', 'Executable path', 'SHA256 hash', 'Email', 'MAC', 'user', 'time'])
        for service in services:
            try:
                binpath = service.as_dict()['binpath']
                binpath = binpath.split(' ', 1)[0]  # Split the path based on the first space character
                
                if i%300 == 0:
                    pro = "■"
                elif i%12 == 0:
                    pro += "■"
                lst_labels[1].configure(text="status : scanning    "+pro)
                parent.update()
                i+=1

                lst_labels[0].configure(text="scanning : "+str(service))
                parent.update()

                hash_value = get_hash(binpath)

                # Get metadata
                file_attributes = win32api.GetFileAttributes(filename)
                time_now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")           
                file_size = os.path.getsize(filename)
                file_extension = os.path.splitext(filename)[1]
                creation_time = os.path.getctime(filename)
                access_time = os.path.getctime(filename)
                modified_time = os.path.getmtime(filename)
                read_only = bool(file_attributes & win32con.FILE_ATTRIBUTE_READONLY)
                writable = not read_only and not bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                executable = bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                is_hidden = bool(file_attributes & win32con.FILE_ATTRIBUTE_HIDDEN)

                writer.writerow([service.name(), binpath, hash_value, parent.username, MAC_address, user, time_now])

                # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
                if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                    dict_hash = {'Hash':hash_value, 'File path':binpath, 'Service name':service.name(), 'email':parent.username, 'MAC':MAC_address, 'user':user, 'time scanned':time_now}
                    thread = threading.Thread(target=upload_dict, args=(dict_hash, lst_labels[2], lst_labels[3], parent, collection))
                    thread.start()
                    
            except Exception as e:
                pass

    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\services_hashes.csv')