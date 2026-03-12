from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="users",
        user="postgres",
        password="2711"
    )
    return conn

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# Form submit route
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/dashboard")

# Dashboard route
@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, email FROM employees")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("dashboard.html", employees=users)

if __name__ == "__main__":
    app.run(debug=True)
