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

def scheduled_tasks(parent, lst_labels, collection, Label):
    # Run the schtasks command to list all scheduled tasks
    output = subprocess.check_output('schtasks.exe /query /fo csv', shell=True)

    # Decode the output as a string and split it into lines
    output = output.decode('utf-8')
    lines = output.splitlines()

    # Additional data
    MAC_address = gma()
    user = getpass.getuser()

    # Use the csv module to create a writer object and write the output to a CSV file

    if lst_labels[2].cget("text") == 'DB status :       connected':
        lst_labels[2].configure(text='DB status :       transmiting data')
        parent.update()

    with open('scheduled_tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Header
        writer.writerow(['TaskName', 'Next Run Time', 'Status', 'email', 'MAC', 'user', 'time scanned'])

        for line in lines:
            time_now = datetime.datetime.now() 
            time_scanned = time_now.strftime("%d/%m/%Y, %H:%M:%S")   
            # Split the line into fields and strip the double quotes from each field
            row = [field.strip('"') for field in line.split(',')]
            if row != ['TaskName', 'Next Run Time', 'Status']:
                row.extend([parent.username, MAC_address, user, time_scanned])
                writer.writerow(row)

                # Send dictonary to MongoDB     USE ONLY IF THERE IS A CONNECTION!
                if lst_labels[2] != 'DB status :       connection failed' and collection != False:
                    dict_hash = {
                        'instance of'   : 'scheduled task',
                        'TaskName'      : row[0], 
                        'Next Run Time' : row[1], 
                        'Status'        : row[2], 
                        'email'         : parent.username, 
                        'MAC'           : MAC_address, 
                        'user'          : user, 
                        'time scanned'  : time_scanned,
                        'scanned time'  : time_now
                    }
                    thread = threading.Thread(target=upload_dict, args=(dict_hash, lst_labels[2], lst_labels[3], parent, collection))
                    thread.start()


    if lst_labels[2].cget("text") != 'DB status :       connection failed' and collection != False:
        lst_labels[3].configure(text='●', fg='#00ff80')
        lst_labels[2].configure(text='DB status :       connected')
    lst_labels[1].configure(text="status : Done!")
    lst_labels[0].configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\scheduled_tasks.csv')