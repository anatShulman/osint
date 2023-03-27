import subprocess
import csv
from CSV_to_MongoDB import *

import tkinter as tk
import subprocess
from tkinter import filedialog

def scheduled_tasks(parent, x, y, Label):
    # Run the schtasks command to list all scheduled tasks
    output = subprocess.check_output('schtasks.exe /query /fo csv', shell=True)

    # Decode the output as a string and split it into lines
    output = output.decode('utf-8')
    lines = output.splitlines()

    # Use the csv module to create a writer object and write the output to a CSV file

    with open('scheduled_tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            # Split the line into fields and strip the double quotes from each field
            row = [field.strip('"') for field in line.split(',')]
            writer.writerow(row)
    y.configure(text="status : Done!")
    parent.update()
    x.configure(text="scanning : None")
    parent.update()

    # upload(os.getcwd()+'\scheduled_tasks.csv')