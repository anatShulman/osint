import tkinter as tk
from GUI import GUI
import time

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Form")

        # Define button styles
        button_style = {'font': ('Arial', 14), 'fg': 'white', 'bg': '#007bff', 'activebackground': '#0062cc', 'padx': 60, 'pady': 0, 'bd': 0}

        # Define label styles
        label_style = {'font': ('Arial', 14), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 0, 'pady': 10}
        label_style1 = {'font': ('Arial', 14), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 0, 'pady': 3}
        label_style2 = {'font': ('Arial', 11), 'fg': 'black', 'bg': '#f5f5f5', 'padx': 0, 'pady': 0}

        # Set the background color of the GUI
        self.configure(bg='#f5f5f5')

        self.geometry("435x445")
        self.minsize(435, 445)
        self.maxsize(435, 445)

        # Add image above login fields
        self.image = tk.PhotoImage(file="exe\Mach_logo.png")
        self.image_label = tk.Label(self, image=self.image, bg='#f5f5f5',pady=10)
        self.image_label.grid(row = 0, column = 0, columnspan = 2, rowspan = 1, padx = 90, pady = 20, sticky='')

        # Add login fields
        self.username_label = tk.Label(self, text="User's Email :", **label_style)
        self.username_label.grid(row=1, column=0, columnspan=1, padx = 15,pady=0, sticky='E')
        self.username_entry = tk.Entry(self, font=('Courier New', 14))
        self.username_entry.grid(row=1, column=1, columnspan=1, pady=0, sticky='W')

        self.password_label = tk.Label(self, text="Password :", **label_style1)
        self.password_label.grid(row=2, column=0, columnspan=1, padx = 15, pady=0, sticky='E')
        self.password_entry = tk.Entry(self, show="*", font=('Courier New', 14))
        self.password_entry.grid(row=2, column=1, columnspan=1, pady=0, sticky='W')

        # Credentials label
        self.credentials_label = tk.Label(self, text="", **label_style2)
        self.credentials_label.grid(row=3, column=0, columnspan=2, padx = 15,pady=0, sticky='')

        # Add login button
        self.login_button = tk.Button(self, text="Sign in", command=self.signin, **button_style)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=2)

    def signin(self):
        # Check if the username and password are correct
        # If correct, destroy the login form and show the GUI form

        

        if self.username_entry.get() == 'username' and self.password_entry.get() == 'password':
            self.destroy()
            gui = GUI()
            gui.geometry(self.geometry())
            gui.mainloop()
        else:
            # self.credentials_label.configure(text="")
            # self.update()
            # time.sleep(0.5)
            self.credentials_label.configure(text="wrong credentials. please try again")
            self.update()


# Create an instance of the login form and run the main loop
login = Login()
login.mainloop()