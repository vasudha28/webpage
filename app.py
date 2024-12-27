from flask import Flask,session,request, jsonify, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] =  "mongodb+srv://vasudha:vasudha@cluster0.0vkno.mongodb.net/bfsi?authSource=admin&retryWrites=true&w=majority&readPreference=primary"
mongo = PyMongo(app)

try:
    client = MongoClient('mongodb+srv://vasudha:vasudha@cluster0.0vkno.mongodb.net/bfsi?authSource=admin&retryWrites=true&w=majority&readPreference=primary')
    db = client.get_database("usersDB")
    print("Databases:", client.list_database_names())
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone'] 
        message = request.form['message']

        
        print(f"Form Data: name={name}, Email={email}, phone={phone}, message={message}")
        
        print("Collections:", mongo.db.list_collection_names())

        
        mongo.db.bfsi.insert_one({'name': name, 'email': email, 'phone': phone,'message':message})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)