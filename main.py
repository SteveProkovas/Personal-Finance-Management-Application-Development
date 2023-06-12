import sqlite3
import tkinter as tk
import os

conn = sqlite3.connect('dbusers.db')
c = conn.cursor()

def check_user_exists(email):
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    result = c.fetchone()
    return result is not None

def create_user(email, password):
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()

def authenticate_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchone()
    return result is not None

def login():
    email = email_entry.get()
    password = password_entry.get()
    if authenticate_user(email, password):
        root.withdraw()
        main_window(email)
    else:
        status_label.config(text="Invalid email or password.", fg="red")

def signup():
    email = email_entry.get()
    password = password_entry.get()
    if check_user_exists(email):
        status_label.config(text="Email already registered.", fg="red")
    else:
        create_user(email, password)
        status_label.config(text="Signup successful!", fg="green")

def main_window(email):
    main_window = tk.Toplevel(root)
    main_window.title("Investment Account")
    main_window.geometry("400x500")
    main_window.state('zoomed')
    main_window.config(bg="#F5F5F5")

    header_label = tk.Label(main_window, text="Investment Account", font=("Helvetica", 20), bg="#F5F5F5", fg="#333333")
    header_label.pack(pady=20)

    user_label = tk.Label(main_window, text=f"Hello {email}! How may I help you?", font=("Helvetica", 14), bg="#F5F5F5", fg="#333333")
    user_label.pack()

    emergency_button = tk.Button(main_window, text="Emergency Fund", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                                 activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                                 command=lambda: show_emergency_options(main_window))
    emergency_button.pack(pady=20)

    debt_button = tk.Button(main_window, text="Debt Payment", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                            activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                            command=lambda: show_debt_options(main_window))
    debt_button.pack()

    investment_button = tk.Button(main_window, text="Investment Account", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                                 activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                                 command=lambda: show_investment_options(main_window))
    investment_button.pack(pady=20)


def show_emergency_options(main_window):
    options_window = tk.Toplevel(main_window)
    options_window.title("Emergency Fund Options")
    options_window.geometry("400x300")
    options_window.state('zoomed')
    #options_window.resizable(False, False)
    options_window.config(bg="#F5F5F5")

    header_label = tk.Label(options_window, text="Emergency Fund Options", font=("Helvetica", 16), bg="#F5F5F5", fg="#333333")
    header_label.pack(pady=20)

    create_button = tk.Button(options_window, text="Create Emergency Fund", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                              activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                              command=lambda: os.startfile('Create Emergency Fund.pdf'))
    create_button.pack(pady=10)

    maximize_button = tk.Button(options_window, text="Maximize Emergency Fund", font=("Helvetica", 14), bg="#2196F3", fg="#FFFFFF",
                                activebackground="#2196F3", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                                command=lambda: os.startfile('Maximize EF.pdf'))
    maximize_button.pack()




def show_debt_options(main_window):
    options_window = tk.Toplevel(main_window)
    options_window.title("Debt Payment Options")
    options_window.geometry("400x300")
    options_window.state('zoomed')
    options_window.config(bg="#F5F5F5")

    header_label = tk.Label(options_window, text="Debt Payment Options", font=("Helvetica", 16), bg="#F5F5F5", fg="#333333")
    header_label.pack(pady=20)

    payment_button = tk.Button(options_window, text="How to Pay Off Debt", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                               activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                               command=lambda: os.startfile('Debt.pdf'))
    payment_button.pack(pady=10)



def show_investment_options(main_window):
    options_window = tk.Toplevel(main_window)
    options_window.title("Investment Account Options")
    options_window.geometry("400x300")
    options_window.state('zoomed')
    options_window.config(bg="#F5F5F5")

    header_label = tk.Label(options_window, text="Investment Account Options", font=("Helvetica", 16), bg="#F5F5F5",
                            fg="#333333")
    header_label.pack(pady=20)

    create_button = tk.Button(options_window, text="Creating an Investment Acc", font=("Helvetica", 14), bg="#4CAF50",
                              fg="#FFFFFF",
                              activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                              command=lambda: os.startfile('Creating IA.pdf'))
    create_button.pack(pady=10)

    maximize_button = tk.Button(options_window, text="Proposed Investments", font=("Helvetica", 14), bg="#2196F3",
                                fg="#FFFFFF",
                                activebackground="#2196F3", activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                                command=lambda: os.startfile('Proposed IA.pdf'))
    maximize_button.pack()


# Create the main window
root = tk.Tk()
root.title("Login or Signup")
root.geometry("400x300")
root.state('zoomed')
#root.resizable(False, False)
root.config(bg="#F5F5F5")

# Create the header label
header_label = tk.Label(root, text="Finance Management", font=("Helvetica", 20), bg="#F5F5F5", fg="#333333")
header_label.pack(pady=20)

# Create the email label and entry widget
email_frame = tk.Frame(root, bg="#F5F5F5")
email_label = tk.Label(email_frame, text="Email:", font=("Helvetica", 14), bg="#F5F5F5", fg="#333333")
email_label.pack(side=tk.LEFT, padx=(20, 10))
email_entry = tk.Entry(email_frame, font=("Helvetica", 14), bg="#FDFDFD", fg="#333333", bd=0, highlightthickness=1, highlightcolor="#333333")
email_entry.pack(side=tk.LEFT, padx=(0, 20), ipadx=10, ipady=8, fill=tk.BOTH, expand=True)
email_frame.pack(fill=tk.BOTH, padx=40, pady=(0, 20))

# Create the password label and entry widget
password_frame = tk.Frame(root, bg="#F5F5F5")
password_label = tk.Label(password_frame, text="Password:", font=("Helvetica", 14), bg="#F5F5F5", fg="#333333")
password_label.pack(side=tk.LEFT, padx=(20, 10))
password_entry = tk.Entry(password_frame, show="*", font=("Helvetica", 14), bg="#FDFDFD", fg="#333333", bd=0, highlightthickness=1, highlightcolor="#333333")
password_entry.pack(side=tk.LEFT, padx=(0, 20), ipadx=10, ipady=8, fill=tk.BOTH, expand=True)
password_frame.pack(fill=tk.BOTH, padx=40, pady=(0, 20))

# Create the login and signup buttons
button_frame = tk.Frame(root, bg="#F5F5F5")
login_button = tk.Button(button_frame, text="Login", font=("Helvetica", 14), bg="#4CAF50", fg="#FFFFFF",
                            activebackground="#4CAF50", activeforeground="#FFFFFF", bd=0, highlightthickness=0, command=login)
login_button.pack(side=tk.LEFT, padx=(20, 10), ipadx=10, ipady=8, fill=tk.BOTH, expand=True)
signup_button = tk.Button(button_frame, text="Signup", font=("Helvetica", 14), bg="#2196F3", fg="#FFFFFF", activebackground="#2196F3",
                            activeforeground="#FFFFFF", bd=0, highlightthickness=0, command=signup)
signup_button.pack(side=tk.LEFT, padx=(0, 20), ipadx=10, ipady=8, fill=tk.BOTH, expand=True)
button_frame.pack(fill=tk.BOTH, padx=40, pady=(0, 20))

# Create the status label
status_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#F5F5F5", fg="red")
status_label.pack()

# Start the Tkinter event loop
root.mainloop()