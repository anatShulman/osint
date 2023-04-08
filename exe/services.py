import psutil
import hashlib
import csv
import os

from getmac import get_mac_address as gma
import getpass
import datetime
import win32api
import win32con
import win32security
import magic

import tkinter as tk
import subprocess
from tkinter import filedialog

import threading

from CSV_to_MongoDB import *
from similarity import *

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
        writer.writerow(['Service name', 'Executable path', 'SHA256 hash', 'SSDEEP', 'TLSH', 'Email', 'MAC', 'user', 'time scanned', 'file size', 'file extension', 'creation time', 'access time', 'modified time', 'read only', 'writable', 'executable', 'hidden'])
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

                # Calculate the hashes of the file contents
                hash_value = get_hash(binpath)
                ssdeep = compute_ssdeep(binpath)
                tlsh = compute_tlsh(binpath)

                # Get metadata
                file_attributes = win32api.GetFileAttributes(binpath)
                magic_obj = magic.Magic()
                file_type = magic_obj.from_file(binpath)
                file_path = os.path.dirname(binpath).replace("\\", "/" )
                time_now = datetime.datetime.now() 
                time_scanned = time_now.strftime("%d/%m/%Y, %H:%M:%S")   
                file_size = os.path.getsize(binpath)
                file_extension = os.path.splitext(binpath)[1].replace('.','')
                creation_time = os.path.getctime(binpath)
                access_time = os.path.getctime(binpath)
                modified_time = os.path.getmtime(binpath)
                read_only = bool(file_attributes & win32con.FILE_ATTRIBUTE_READONLY)
                readable = bool(file_attributes & win32con.GENERIC_READ)
                writable = not read_only and not bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                executable = bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                is_hidden = bool(file_attributes & win32con.FILE_ATTRIBUTE_HIDDEN)
                
                writer.writerow([service.name(), file_path, hash_value, ssdeep, tlsh, parent.username, MAC_address, user, time_now, file_size, file_extension, creation_time, access_time, modified_time, read_only, writable, executable, is_hidden])

                # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
                if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                    dict_hash = {
                        'sha256'         : hash_value,
                        'ssdeep'         : ssdeep,
                        'tlsh'           : tlsh,
                        'file path'      : file_path,
                        'file name'      : service.name(),
                        'file type'      : file_type,
                        'email'          : parent.username,
                        'MAC'            : MAC_address,
                        'user'           : user,
                        'time scanned'   : time_scanned,
                        'scanned time'   : time_now,
                        'file size'      : file_size,
                        'file extension' : file_extension,
                        'creation time'  : creation_time,
                        'access time'    : access_time,
                        'modified time'  : modified_time,
                        'read only'      : read_only,
                        'readable'       : readable,
                        'writable'       : writable,
                        'executable'     : executable,
                        'hidden'         : is_hidden
                    }
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