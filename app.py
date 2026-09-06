from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -------------------------
# Database
# -------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            "INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com')"
        )
        cursor.execute(
            "INSERT INTO users (username, email) VALUES ('student', 'student@example.com')"
        )

    conn.commit()
    conn.close()


# -------------------------
# Home
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -------------------------
# File Upload
# -------------------------
@app.route("/upload", methods=["GET", "POST"])
def upload():
    message = ""

    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename:
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            message = f"File uploaded successfully: {uploaded_file.filename}"

    return render_template("upload.html", message=message)


# -------------------------
# OS Command Injection
# -------------------------
@app.route("/command", methods=["GET", "POST"])
def command():
    result = ""

    if request.method == "POST":
        command_input = request.form.get("command", "")

        try:
            result = subprocess.check_output(
                command_input,
                shell=True,
                stderr=subprocess.STDOUT,
                text=True
            )
        except Exception as e:
            result = str(e)

    return render_template("command.html", result=result)


# -------------------------
# XSS + SQL Injection
# -------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "")

    results = []

    if query:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        sql = "SELECT id, username, email FROM users WHERE username LIKE ?"

        try:
            cursor.execute(sql, ('%' + query + '%',))
            results = cursor.fetchall()
        except Exception as e:
            results = [(0, "Database Error", str(e))]

        conn.close()

    return render_template(
        "search.html",
        query=query,
        results=results
    )


if __name__ == "__main__":
    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
