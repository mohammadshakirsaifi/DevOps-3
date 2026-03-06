from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "your_mongodb_connection_string"
client = MongoClient(MONGO_URI)
db = client["flaskdb"]
collection = db["users"]

# API Route
@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

# Form page
@app.route('/')
def index():
    return render_template("index.html")

# Form submission
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template("index.html", error=str(e))

# Success page
@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
