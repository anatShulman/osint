import tkinter as tk
import subprocess
from tkinter import filedialog
import os

# scripts we've written
from hash import *
from processes import processes_hash
from services import *
from schtasks import scheduled_tasks
from sockests import netstat

# Define the directory of the scripts
scripts_directory = os.getcwd()

def run_script(script_path):
    subprocess.run(['python', script_path], cwd=scripts_directory)

def choose_directory():
    global working_directory
    directory_path = filedialog.askdirectory()
    if directory_path:
        working_directory = directory_path
        directory_label.config(text=working_directory)

# Create the GUI
root = tk.Tk()
root.title('Risks\' agent')

# Define button styles
button_style = {'font': ('Arial', 14), 'fg': 'white', 'bg': '#007bff', 'activebackground': '#0062cc', 'padx': 20, 'pady': 10, 'bd': 0}

# Define label styles
label_style = {'font': ('Arial', 12), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 10, 'pady': 10}

# Define the working directory
working_directory = os.getcwd()

# Create a label to display the chosen directory
directory_label = tk.Label(root, **label_style)
directory_label.config(text=scripts_directory)
directory_label.grid(row=0, column=0, columnspan=2, sticky='we')

# Create a button to choose a directory
choose_directory_button = tk.Button(root, text='Choose Directory', command=choose_directory, **button_style)
choose_directory_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create some "lorem ipsum" text
lorem_ipsum = '1. Please choose directory in which you wish to check for risks\n2. Now choose the system\'s resources you want to scan:          '

lorem_ipsum_label = tk.Label(root, text=lorem_ipsum, wraplength=600, **label_style)
lorem_ipsum_label.grid(row=2, column=0, columnspan=2, pady=10)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()

# create checkboxes with labels
check1 = tk.Checkbutton(root, text="Hashing all files (in currnet directory)", variable=var1, font=("Arial",13))
check2 = tk.Checkbutton(root, text="Hashing running processes", variable=var2, font=("Arial",13))
check3 = tk.Checkbutton(root, text="Hashing running services", variable=var3, font=("Arial",13))
check4 = tk.Checkbutton(root, text="Get scheduoed tasks", variable=var4, font=("Arial",13))
check5 = tk.Checkbutton(root, text="Get all network connections", variable=var5, font=("Arial",13))

# layout the checkboxes using grid
check1.grid(row=3, column=1, sticky="w",padx=0, pady=0)
check2.grid(row=4, column=1, sticky="w",padx=0, pady=0)
check3.grid(row=5, column=1, sticky="w",padx=0, pady=0)
check4.grid(row=6, column=1, sticky="w",padx=0, pady=0)
check5.grid(row=7, column=1, sticky="w",padx=0, pady=0)

def button6_callback():
    if var1.get() == True:
        get_hashes(working_directory)
    if var2.get() == True:
        processes_hash()
    if var3.get() == True:
        services_hash()
    if var4.get() == True:
        scheduled_tasks()
    if var5.get() == True:
        netstat()

# Create the buttons
button6 = tk.Button(root, text='Activate scan', command=button6_callback, **button_style)

# Add the buttons to the GUI

button6.grid(row=8, column=1, padx=0, pady=20)

# Set the background color of the GUI
root.configure(bg='#f5f5f5')

# Start the GUI event loop
root.mainloop()