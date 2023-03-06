import tkinter as tk
import subprocess
from tkinter import filedialog
import os

from hash import *

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

# Define the button callbacks
def button1_callback():
    get_hashes(working_directory)

def button2_callback():
    run_script('schtasks.py')

def button3_callback():
    run_script('processes.py')

def button4_callback():
    run_script('sockests.py')

def button5_callback():
    run_script('services.py')

def button6_callback():
    run_script('virustotal_agent.py')

# Create the buttons
button1 = tk.Button(root, text='Hasing all files \n', command=button1_callback, **button_style)
button2 = tk.Button(root, text='Get scheduled\n tasks', command=button2_callback, **button_style)
button3 = tk.Button(root, text='Hasing running\nProcesses', command=button3_callback, **button_style)
button4 = tk.Button(root, text='Get all network\nconnections', command=button4_callback, **button_style)
button5 = tk.Button(root, text='Hasing running\nServices', command=button5_callback, **button_style)
button6 = tk.Button(root, text='Send files\n  to VirusTotal  ', command=button6_callback, **button_style)

# Add the buttons to the GUI
button1.grid(row=3, column=0, padx=20, pady=10)
button2.grid(row=3, column=1, padx=20, pady=10)
button3.grid(row=4, column=0, padx=20, pady=10)
button4.grid(row=4, column=1, padx=20, pady=10)
button5.grid(row=5, column=0, padx=20, pady=10)
button6.grid(row=5, column=1, padx=20, pady=10)

# Set the background color of the GUI
root.configure(bg='#f5f5f5')

# Start the GUI event loop
root.mainloop()