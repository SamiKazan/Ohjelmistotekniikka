from tkinter import ttk, StringVar, constants
from services.main_service import budgeting_service


class CreateaccountUI:
    def __init__(self, root, handle_create_user, handle_show_login_UI):
        self.root = root
        self.handle_create_user = handle_create_user
        self.handle_show_login_UI = handle_show_login_UI
        self.frame = None
        self.enter_username = None
        self.enter_password = None

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def creation_handler(self):
        username = self.enter_username.get()
        password = self.enter_password.get()

        if len(username) < 3:
            raise KeyError("Username must be atleast 3 characters long")
        if len(password) < 5:
            raise KeyError("Password must be atleast 5 characters long")

        try:
            budgeting_service.create_account(username, password)
            self.handle_create_user()
        except:
            print("Failed to create account (UI)")

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

        # kysyin copilotilta miten saan yhdelle napille monta komentoa
        create_user_button = ttk.Button(master=self.frame, text="Create user",
                                        command=lambda: [self.creation_handler(), self.handle_create_user()])
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        cancel_button = ttk.Button(master=self.frame, text="Cancel",
                                   command=self.handle_show_login_UI)
        cancel_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=2, minsize=600)
