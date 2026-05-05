from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user="appuser",
        password=os.environ.get("DB_PASSWORD"),
        database="testdb"
    )

@app.route("/")
def home():
    return "API Flask + MySQL avec Docker"

@app.route("/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (data["name"],))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Item ajouté"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)