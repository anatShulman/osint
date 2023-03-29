import tkinter as tk
import subprocess
from tkinter import filedialog
import os
import time
import threading

# scripts we've written
from hash import *
from processes import processes_hash
from services import *
from schtasks import scheduled_tasks
from sockests import netstat
from pymongo import *

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
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

        self.title('Risks\' agent')

        # Define button styles
        button_style = {'font': ('Arial', 14), 'fg': 'white', 'bg': '#007bff', 'activebackground': '#0062cc', 'padx': 20, 'pady': 10, 'bd': 0}

        # Define label styles
        label_style = {'font': ('Arial', 12), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 0, 'pady': 0}

        # Define the working directory
        working_directory = os.getcwd()

        # Create a label to display the chosen directory
        directory_label = tk.Label(self, **label_style)
        directory_label.config(text=scripts_directory)
        directory_label.grid(row=0, column=0, columnspan=2, sticky='we')

        # Create a button to choose a directory
        choose_directory_button = tk.Button(self, text='Choose Directory', command=choose_directory, **button_style)
        choose_directory_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Create some "lorem ipsum" text
        lorem_ipsum = '1. Please choose directory in which you wish to check for risks\n2. Now choose the system\'s resources you want to scan:          '

        lorem_ipsum_label = tk.Label(self, text=lorem_ipsum, wraplength=600, **label_style)
        lorem_ipsum_label.grid(row=2, column=0, columnspan=2, pady=10)

        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        var3 = tk.BooleanVar()
        var4 = tk.BooleanVar()
        var5 = tk.BooleanVar()

        # create checkboxes with labels
        check1 = tk.Checkbutton(self, text="Hashing all files (in currnet directory)", variable=var1, **label_style)
        check2 = tk.Checkbutton(self, text="Hashing running processes", variable=var2, **label_style)
        check3 = tk.Checkbutton(self, text="Hashing running services", variable=var3, **label_style)
        check4 = tk.Checkbutton(self, text="Get scheduoed tasks", variable=var4, **label_style)
        check5 = tk.Checkbutton(self, text="Get all network connections", variable=var5, **label_style)

        # layout the checkboxes using grid
        check1.grid(row=3, column=1, sticky="w",padx=0, pady=0)
        check2.grid(row=4, column=1, sticky="w",padx=0, pady=0)
        check3.grid(row=5, column=1, sticky="w",padx=0, pady=0)
        check4.grid(row=6, column=1, sticky="w",padx=0, pady=0)
        check5.grid(row=7, column=1, sticky="w",padx=0, pady=0)

        def run_button6_callback():
            # Run button6_callback on a separate thread
            t = threading.Thread(target=button6_callback)
            t.start()

        def button6_callback():
            if var1.get() == True:
                status_label.configure(text="status : pending")
                self.update()
                get_hashes(self, [scannig_label, status_label, db_label, circle_label], collection, tk.Label, working_directory)
                
            if var2.get() == True:
                status_label.configure(text="status : pending")
                self.update()
                processes_hash(parent=self, x = scannig_label, y = status_label, Label=tk.Label)
            
            if var3.get() == True:
                status_label.configure(text="status : pending")
                self.update()
                services_hash(parent=self, x = scannig_label, y = status_label, Label=tk.Label)
            
            if var4.get() == True:
                status_label.configure(text="status : pending")
                self.update()
                scheduled_tasks(parent=self, x = scannig_label, y = status_label, Label=tk.Label)
            
            if var5.get() == True:
                status_label.configure(text="status : pending")
                self.update()
                netstat(parent=self, x = scannig_label, y = status_label, Label=tk.Label)


        # Create the buttons
        button6 = tk.Button(self, text='Activate scan', command=run_button6_callback, **button_style)

        # Add the buttons to the GUI

        button6.grid(row=8, column=1, padx=0, pady=20)

        # Labels
        # db_label = tk.Label(self, text='DB status : establishing', wraplength=0, **label_style)
        # db_label.place(relx = 0.0,rely = 1.0,y=-40,anchor ='sw')



        db_label = tk.Label(self, text='DB status :       establishing', wraplength=0, **label_style)
        circle_label = tk.Label(self, text='●', wraplength=0, font=('Arial', 24),fg='#ffea00', bg= '#f5f5f5')
        db_label.place(relx = 0.0,rely = 1.0,y=-40,anchor ='sw')
        circle_label.place(relx = 0.0,rely = 1.0,y=-32, x=82, anchor ='sw')

        status_label = tk.Label(self, text='status : ready to scan', wraplength=0, **label_style)
        status_label.place(relx = 0.0,rely = 1.0,y=-20,anchor ='sw')

        scannig_label = tk.Label(self, text='scanning : None', wraplength=0, anchor ='w', **label_style)
        scannig_label.place(relx = 0.0,rely = 1.0,anchor ='sw')

        # Set the background color of the GUI
        self.configure(bg='#f5f5f5')

        self.geometry("435x445")
        self.minsize(435, 445)
        self.maxsize(435, 445)

        # Start the GUI event loop

        collection = False

        def connection():
            # time.sleep(2)
            global collection
            collection = check_connection()
            if collection == False:
                db_label.configure(text='DB status :       connection failed')
                circle_label.configure(fg='red')
                self.update()
            else:
                db_label.configure(text='DB status :       connected')
                circle_label.configure(fg='#00ff80')
                self.update()
            return

        thread = threading.Thread(target=connection)
        thread.start()

        self.mainloop()


