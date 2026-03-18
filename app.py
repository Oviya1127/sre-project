from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="",
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
    cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/dashboard")

# Dashboard route
@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
