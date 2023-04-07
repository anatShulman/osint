import os
import hashlib
import csv

import tkinter as tk
import subprocess
from tkinter import filedialog

from getmac import get_mac_address as gma
import getpass
import datetime
import win32api
import win32con
import win32security
import magic

import threading

from CSV_to_MongoDB import *

def get_subdirectories(directory):
    #Traverse recursively through a given path and creates a list representing the file-tree from that path.
    subdirectories = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            subdirectories.append(file_path)
            subdirectories.extend(get_subdirectories(file_path))
    return subdirectories

def get_hashes(parent, lst_labels, collection, Label, directory = 'Z:\Public'):
    #Hashes all the currently running processes on the system into a csv file
    #Using SHA256 algorithm
    dirs = [directory]
    dirs.extend(get_subdirectories(directory))

    i = 0

    hashes = []

    # Additional metadata
    MAC_address = gma()
    user = getpass.getuser()
 

    for file_path in dirs:
        for filename in os.listdir(file_path):
            try:
                if os.path.isfile(file_path+'/'+filename):   
                    # Label text     
                    if i%300 == 0:
                        pro = "■"
                    elif i%12 == 0:
                        pro += "■"
                    lst_labels[1].configure(text="status : scanning    "+pro)
                    parent.update()
                    i+=1

                    lst_labels[0].configure(text="scanning : "+'/'+filename)
                    parent.update()
                    with open(file_path+'/'+filename, 'rb') as file:
                        file_contents = file.read()

                    # Calculate the hash of the file contents
                    file_hash = hashlib.sha256(file_contents).hexdigest()

                    # Get metadata
                    file_attributes = win32api.GetFileAttributes(file_path+'/'+filename)
                    magic_obj = magic.Magic()
                    file_type = magic_obj.from_file(file_path+'/'+filename)
                    time_now = datetime.datetime.now() 
                    time_scanned = time_now.strftime("%d/%m/%Y, %H:%M:%S")    
                    file_size = os.path.getsize(file_path+'/'+filename)
                    file_extension = os.path.splitext(file_path+'/'+filename)[1]
                    creation_time = os.path.getctime(file_path+'/'+filename)
                    access_time = os.path.getctime(file_path+'/'+filename)
                    modified_time = os.path.getmtime(file_path+'/'+filename)
                    read_only = bool(file_attributes & win32con.FILE_ATTRIBUTE_READONLY)
                    readable = bool(file_attributes & win32con.GENERIC_READ)
                    writable = not read_only and not bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                    executable = bool(file_attributes & win32con.FILE_ATTRIBUTE_DIRECTORY)
                    is_hidden = bool(file_attributes & win32con.FILE_ATTRIBUTE_HIDDEN)


                    # Add the hash and filename to the list
                    hashes.append((file_hash, file_path.replace("\\", "/" ), filename, file_type, parent.username, MAC_address, user, time_scanned, time_now, file_size, file_extension, creation_time, access_time, modified_time, read_only, readable, writable, executable, is_hidden))
                    
                    # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
                    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                        dict_hash = {
                            'hash'           : file_hash,
                            'file path'      : file_path,
                            'file name'      : filename,
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

            except:
                pass
    
    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # Open a CSV file for writing
    with open('hashes.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Hash', 'File path','File name', 'File type', 'Email', 'MAC', 'user', 'time scanned', 'scanned time', 'file size', 'file extension', 'creation time', 'access time', 'modified time', 'read only', 'readable', 'writable', 'executable', 'hidden'])
        for hash_tuple in hashes:
            writer.writerow(hash_tuple)

    # upload(os.getcwd()+'\hashes.csv')
