import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create an instance of flask and assign it to the app variable
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'coworkingSpacesDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

# this will be the default function that will be called when the application is run
@app.route('/')
@app.route('/get_coworkingspaces')
def get_coworkingspaces():
    return render_template('home.html', coworkingspaces=mongo.db.coworkingspaces.find())
  
    
@app.route('/add_coworkingspace')
def add_coworkingspace():
    return render_template('addspace.html', cities=mongo.db.cities.find())
   
    
@app.route('/insert_coworkingspace', methods=['POST'])
def insert_coworkingspace():
    coworkingspaces = mongo.db.coworkingspaces
    coworkingspaces.insert_one(request.form.to_dict())
    return redirect(url_for('get_coworkingspaces'))
    

@app.route('/edit_coworkingspace/<coworkingspace_id>')
def edit_coworkingspace(coworkingspace_id):
    the_coworkingspace =  mongo.db.coworkingspaces.find_one({"_id": ObjectId(coworkingspace_id)})
    all_cities =  mongo.db.cities.find()
    return render_template('editspace.html', coworkingspace=the_coworkingspace,
                           cities=all_cities)
                           
@app.route("/delete_coworkingspace/<coworkingspace_id>")
def delete_coworkingspace(coworkingspace_id):
    mongo.db.coworkingspaces.remove({'_id': ObjectId(coworkingspace_id)})
    return redirect(url_for('get_coworkingspaces'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            