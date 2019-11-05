import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create an instance of flask and assign it to the app variable
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'coworkingSpacesDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# this will be the default function that will be called when the application is run
@app.route('/')
@app.route('/get_coworkingspaces')
def get_coworkingspaces():
    return render_template('home.html', coworkingspaces=mongo.db.coworkingspaces.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            