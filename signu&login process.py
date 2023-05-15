from collections import UserDict
from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('dbusers.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = c.fetchone()
        if user is not None:
            session['user_id'] = user[0]
            return redirect('/dashboard')
        else:
            return "Invalid email or password"
    else:
        if 'user_id' in session:
            return redirect('/dashboard')
        else:
            return '''
                <form method="POST">
                    <input type="email" name="email" placeholder="Email" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">Login</button>
                    <a href="/register">Register</a>
                </form>
            '''


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('dbusers.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        if c.fetchone() is not None:
            return "Email already exists"
        else:
            c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            user_id = c.lastrowid
            session['user_id'] = user_id
            return redirect('/dashboard')
    else:
        if 'user_id' in session:
            return redirect('/dashboard')
        else:
            return '''
                <form method="POST">
                    <input type="email" name="email" placeholder="Email" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">Register</button>
                </form>
            '''


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        conn = sqlite3.connect('dbusers.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
        user = c.fetchone()
        return f"Welcome, {user[1]}"
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
