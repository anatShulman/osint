import tkinter as tk
import subprocess
from tkinter import filedialog
import os
import time
import threading
import base64
import win32api
import win32con
from encoded import ssdeep_string
import sys

# scripts we've written
from hash import *
from processes import processes_hash
from services import *
from schtasks import scheduled_tasks
from sockests import netstat
from pymongo import *

import requests
import datetime

class GUI(tk.Tk):
    def __init__(self, username):
        super().__init__()
        # Define the directory of the scripts
        scripts_directory = os.getcwd()
        
        self.username=username

        def run_script(script_path):
            subprocess.run(['python', script_path], cwd=scripts_directory)

        def choose_directory():
            global working_directory
            directory_path = filedialog.askdirectory()
            if directory_path:
                working_directory = directory_path
                self.directory_label.config(text=working_directory)

        def restart_program():
            python = sys.executable
            os.execl(python, python, *sys.argv)

        def stop_and_restart():
            self.destroy()
            restart_program()

        self.title('Risks\' agent')

        # Define button styles
        button_style = {'font': ('Arial', 14), 'fg': 'white', 'bg': '#759bc2', 'activebackground': '#323d5e', 'padx': 20, 'pady': 10, 'bd': 0}
        stop_button_style = {'font': ('Arial', 15), 'fg': 'dark red', 'bg': 'red', 'activebackground': '#323d5e', 'padx': 0, 'pady': 0, 'bd': 0}

        # Define label styles
        label_style = {'font': ('Arial', 12), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 0, 'pady': 0}

        # Define the working directory
        working_directory = os.getcwd()

        # Create a label to display the chosen directory
        self.directory_label = tk.Label(self, **label_style)
        self.directory_label.config(text=scripts_directory)
        self.directory_label.grid(row=0, column=0, columnspan=2, sticky='we')

        # Create a button to choose a directory
        self.choose_directory_button = tk.Button(self, text='Choose Directory', command=choose_directory, **button_style)
        self.choose_directory_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Create some "lorem ipsum" text
        lorem_ipsum = '1. Please choose directory in which you wish to check for risks\n2. Now choose the system\'s resources you want to scan:          '

        self.lorem_ipsum_label = tk.Label(self, text=lorem_ipsum, wraplength=600, **label_style)
        self.lorem_ipsum_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        self.var4 = tk.BooleanVar()
        self.var5 = tk.BooleanVar()

        # create checkboxes with labels
        self.check1 = tk.Checkbutton(self, text="Hashing all files (in currnet directory)", variable=self.var1, **label_style)
        self.check2 = tk.Checkbutton(self, text="Hashing running processes", variable=self.var2, **label_style)
        self.check3 = tk.Checkbutton(self, text="Hashing running services", variable=self.var3, **label_style)
        self.check4 = tk.Checkbutton(self, text="Get scheduled tasks", variable=self.var4, **label_style)
        self.check5 = tk.Checkbutton(self, text="Get network connections & URL history", variable=self.var5, **label_style)

        # layout the checkboxes using grid
        self.check1.grid(row=3, column=1, sticky="w",padx=0, pady=0)
        self.check2.grid(row=4, column=1, sticky="w",padx=0, pady=0)
        self.check3.grid(row=5, column=1, sticky="w",padx=0, pady=0)
        self.check4.grid(row=6, column=1, sticky="w",padx=0, pady=0)
        self.check5.grid(row=7, column=1, sticky="w",padx=0, pady=0)

        


        # Create the buttons
        self.button6 = tk.Button(self, text='Activate scan', command=self.run_button6_callback, **button_style)
        self.restart_button = tk.Button(self, text="∎∎", command=stop_and_restart, **stop_button_style)
        # Add the buttons to the GUI

        self.button6.grid(row=8, column=1, padx=0, pady=20)
        self.restart_button.grid(row=8, column=0, padx=0, pady=0)

        # Labels
        # db_label = tk.Label(self, text='DB status : establishing', wraplength=0, **label_style)
        # db_label.place(relx = 0.0,rely = 1.0,y=-40,anchor ='sw')



        self.db_label = tk.Label(self, text='DB status :       establishing connection ...', wraplength=0, **label_style)
        self.circle_label = tk.Label(self, text='●', wraplength=0, font=('Arial', 24),fg='#ffea00', bg= '#f5f5f5')
        self.db_label.place(relx = 0.0,rely = 1.0,y=-40,anchor ='sw')
        self.circle_label.place(relx = 0.0,rely = 1.0,y=-32, x=82, anchor ='sw')

        self.status_label = tk.Label(self, text='status : ready to scan', wraplength=0, **label_style)
        self.status_label.place(relx = 0.0,rely = 1.0,y=-20,anchor ='sw')

        self.scannig_label = tk.Label(self, text='scanning : None', wraplength=0, anchor ='w', **label_style)
        self.scannig_label.place(relx = 0.0,rely = 1.0,anchor ='sw')

        # Set the background color of the GUI
        self.configure(bg='#f5f5f5')

        self.geometry("435x445")
        self.minsize(435, 445)
        self.maxsize(435, 445)

        # Start the GUI event loop

        collection = False

        thread = threading.Thread(target=self.connection)
        thread.start()

        self.mainloop()

    def run_button6_callback(self):
        # Run button6_callback on a separate thread
        t = threading.Thread(target=self.button6_callback)
        t.start()

    def button6_callback(self):
        # decode the base64-encoded string of .exe
        decoded_data = base64.b64decode(ssdeep_string())
        # write the decoded data to a hidden file
        try:
            with open("ssdeep.exe", 'wb') as f: 
                f.write(decoded_data)
                
            # set the file attributes to hidden
            win32api.SetFileAttributes("ssdeep.exe", win32con.FILE_ATTRIBUTE_HIDDEN)
        except:
            pass
        
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        
        if self.var1.get() == True:   
            self.status_label.configure(text="status : pending ...")
            self.update()
            get_hashes(self, [self.scannig_label, self.status_label, self.db_label, self.circle_label], collection, tk.Label, working_directory)
            
        if self.var2.get() == True:
            self.status_label.configure(text="status : pending ...")
            self.update()
            processes_hash(self, [self.scannig_label, self.status_label, self.db_label, self.circle_label], collection, tk.Label)
        
        if self.var3.get() == True:
            self.status_label.configure(text="status : pending ...")
            self.update()
            services_hash(self, [self.scannig_label, self.status_label, self.db_label, self.circle_label], collection, tk.Label)
        
        if self.var4.get() == True:
            self.status_label.configure(text="status : pending ...")
            self.update()
            scheduled_tasks(self, [self.scannig_label, self.status_label, self.db_label, self.circle_label], collection, tk.Label)
        
        if self.var5.get() == True: 
            self.status_label.configure(text="status : pending ...")
            self.update()
            netstat(self, [self.scannig_label, self.status_label, self.db_label, self.circle_label], collection, tk.Label)

        if self.db_label.cget("text") == 'DB status :       transmiting data':
            self.db_label.configure(text='DB status :       connected')
            self.update()

        # get all hashes after 'date' by this email
        if (self.var1.get() == True) or (self.var2.get() == True) or (self.var3.get() == True):
            # POST to back server, notify that URLs sent
            data = {'email':self.username, 'date':date}
            thread = threading.Thread(target=requests.post, args=('http://localhost:5000/hashes', data))
            thread.start()

        try:
            os.remove("ssdeep.exe")
        except:
            pass

    def connection(self):
        # time.sleep(2)
        global collection
        collection = check_connection()
        if collection == False:
            self.db_label.configure(text='DB status :       connection failed')
            self.circle_label.configure(fg='red')
            self.update()
        else:
            self.db_label.configure(text='DB status :       connected')
            self.circle_label.configure(fg='#00ff80')
            self.update()
        return




