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

import re
from browser_history import get_history

import threading
import requests


def netstat(parent, lst_labels, collection, Label):
    MAC_address = gma()
    user = getpass.getuser()
    time_now = datetime.datetime.now() 
    time_scanned = time_now.strftime("%d/%m/%Y, %H:%M:%S")   
    # Run netstat command and capture output
    output = subprocess.check_output(["netstat", "-n"], creationflags=subprocess.CREATE_NO_WINDOW).decode()

    if lst_labels[2].cget("text") == 'DB status :       connected':
        lst_labels[2].configure(text='DB status :       transmiting data')
        parent.update()

    # Find all valid IP addresses with ports in the output
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b')
    ip_list = pattern.findall(output)

    # Filter out non-public IPs and remove duplicates
    filtered_ips = set()
    for ip in ip_list:
        ip_address, port = ip.split(':')
        if ip_address.startswith(('10.', '172.16.', '192.168.', '169.254.', '127.')):
            # Ignore non-public IPs
            continue
        elif ip_address == 'localhost':
            # Replace localhost with actual IP address
            ip_address = '127.0.0.1'
        elif ip_address == '::1':
            # Ignore IPv6 loopback address
            continue
        else:
            # Add valid public IP to filtered list
            filtered_ips.add(ip_address)

    # Convert filtered_ips set to list and print
    ip_list = list(filtered_ips)
    url_list = list(get_history().sort_domain().keys())

    # Drop strings without '.'
    url_list = [s for s in url_list if '.' in s]
    # Drop strings starting with 'localhost'
    url_list = [s for s in url_list if not s.startswith('localhost')]

    # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
    if lst_labels[2] != 'DB status :       connection failed' and collection != False:
        dict_ip = {
            'instance of'   : 'network connection',
            'ip list'       : ip_list,
            'url list'      : url_list,
            'email'         : parent.username,
            'MAC'           : MAC_address,
            'user'          : user,
            'time scanned'  : time_scanned,
            'scanned time'  : time_now
        }
        thread = threading.Thread(target=upload_dict, args=(dict_ip, lst_labels[2], lst_labels[3], parent, collection))
        thread.start()
        
        # POST to back server, notify that URLs sent
        data = {'email':parent.username, 'date':time_scanned}
        thread = threading.Thread(target=requests.post, args=('http://localhost:5000/network-connections', data))
        thread.start()

    # Use the csv module to create a writer object and write the data to a CSV file
    with open('netstat.csv', 'w', newline='') as csvfile:
        fieldnames = {
            'ip list': ",".join(ip_list),
            'url list': ",".join(url_list),
            'email': parent.username,
            'MAC': MAC_address,
            'user': user,
            'time scanned': time_scanned,
        }
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames.keys())
        writer.writerow(fieldnames.values())

    if lst_labels[2].cget("text") != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\netstat.csv')