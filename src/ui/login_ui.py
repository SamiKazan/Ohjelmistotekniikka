from tkinter import ttk, constants
from services.main_service import budgeting_service


class LoginUI:
    """user interface for logging in
    """
    def __init__(self, root, handle_login, handle_show_create_account_UI):
        """Class construcotr creats login page

        Args:
            root:
                TKinter-element, page view initialization
            handle_login:
                callable, called when trying to login
            handle_show_create_account_UI:
                callable, shows create_account page on call
        """
        self.root = root
        self.handle_login = handle_login
        self.handle_show_create_account_UI = handle_show_create_account_UI
        self.frame = None
        self.enter_username = None
        self.enter_password = None

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def login_handler(self):
        username = self.enter_username.get()
        password = self.enter_password.get()

        user = budgeting_service.login(username, password)
        
        if user != None:
            self.handle_login()
        else:
            print("wrong username or password (UI)")

    def username_input(self):
        label = ttk.Label(master=self.frame, text="Username")

        self.enter_username = ttk.Entry(master=self.frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_username.grid(padx=5, pady=5, sticky=constants.EW)

    def password_input(self):
        label = ttk.Label(master=self.frame, text="Password")

        self.enter_password = ttk.Entry(master=self.frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_password.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.username_input()
        self.password_input()

        # tehty github copilotilla
        login_button = ttk.Button(
            self.frame, text="Login", command=self.login_handler)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        create_user_button = ttk.Button(master=self.frame, text="Dont have Account? Create one here",
                                        command=self.handle_show_create_account_UI)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        # loppuu

        self.frame.grid_columnconfigure(0, weight=2, minsize=800)
