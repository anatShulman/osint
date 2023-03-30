import psutil
import subprocess
import csv
from CSV_to_MongoDB import *

import tkinter as tk
import subprocess
from tkinter import filedialog

from getmac import get_mac_address as gma
import getpass
import datetime

import threading

def netstat(parent, lst_labels, collection, Label):
    # Run the netstat command to get a list of all active connections
    output = subprocess.check_output('netstat -ano', shell=True)

    # Decode the output as a string and split it into lines
    output = output.decode('utf-8')
    lines = output.splitlines()

    # Extract information about each connection and store it in a list
    data = []

    # Additional data
    MAC_address = gma()
    user = getpass.getuser()

    for line in lines:
        line = line.strip()
        if line.startswith('TCP') or line.startswith('UDP'):
            parts = line.split()
            proto = parts[0]
            local_addr = parts[1]
            remote_addr = parts[2]
            state = parts[3]
            pid = parts[-1]

            time_now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            data.append({'proto': proto, 'local_addr': local_addr, 'remote_addr': remote_addr, 'state': state, 'pid': pid, 'email':parent.username, 'MAC':MAC_address, 'user':user, 'time scanned':time_now})

            # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
            if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                dict_hash = {'protocol': proto, 'local address': local_addr, 'remote address': remote_addr, 'state': state, 'PID': pid, 'email':parent.username, 'MAC':MAC_address, 'user':user, 'time scanned':time_now}
                thread = threading.Thread(target=upload_dict, args=(dict_hash, lst_labels[2], lst_labels[3], parent, collection))
                thread.start()

    # Use the csv module to create a writer object and write the data to a CSV file
    with open('netstat.csv', 'w', newline='') as csvfile:
        fieldnames = ['proto', 'local_addr', 'remote_addr', 'state', 'pid', 'url', 'email', 'MAC', 'user', 'time scanned']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            # Use the pid to get information about the process, including its executable path
            try:
                p = psutil.Process(int(d['pid']))
                url = ''
                try:
                    url = p.exe()
                except psutil.AccessDenied:
                    pass
                d['url'] = url
            except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError):
                pass
            writer.writerow(d)

    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\netstat.csv')