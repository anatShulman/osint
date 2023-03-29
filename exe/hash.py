import os
import hashlib
import csv

import tkinter as tk
import subprocess
from tkinter import filedialog

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

                    # Add the hash and filename to the list
                    hashes.append((file_hash, file_path, filename))

                    # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
                    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                        dict_hash = {'Hash':file_hash, 'File path':file_path,'File name':filename}
                        thread = threading.Thread(target=upload_dict, args=(dict_hash, lst_labels[2], lst_labels[3], parent, collection))
                        thread.start()

            except:
                pass
    lst_labels[1].configure(text="status : Done!")
    parent.update()
    lst_labels[0].configure(text="scanning : None")
    parent.update()


    # Open a CSV file for writing
    with open('hashes.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Hash', 'File path','File name'])
        for hash_tuple in hashes:
            writer.writerow(hash_tuple)

    # upload(os.getcwd()+'\hashes.csv')
