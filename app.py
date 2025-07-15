from flask import Flask, render_template,request,redirect
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='login',
        buffered=True
    )

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/quotes')
def quotes():
    return render_template('quotes.html') 

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    return 'Submitted'
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn= get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cur.close()
        return redirect('/login')
    return render_template('signup.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['Password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        if user:
            return render_template('index.html')
        else:
            return "Invalid username or password"
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)

