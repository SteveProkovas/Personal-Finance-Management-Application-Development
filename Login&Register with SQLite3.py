import sqlite3

conn = sqlite3.connect('dbusers.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT UNIQUE,
              password TEXT)''')


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


while True:
    choice = input("Enter 'login' to login or 'signup' to sign up: ")

    if choice.lower() == "login":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if authenticate_user(email, password):
            print("Login successful!")
        else:
            print("Invalid email or password.")

    elif choice.lower() == "signup":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if check_user_exists(email):
            print("Email already registered.")
        else:
            create_user(email, password)
            print("Signup successful!")

    else:
        print("Invalid choice. Please try again.")
