import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create an instance of flask and assign it to the app variable
app = Flask(__name__)

# Environment variables
app.config["MONGO_DBNAME"] = 'coworkingSpacesDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

# this will be the default function that will be called when the application is run
@app.route('/')
@app.route('/get_coworkingspaces')
def get_coworkingspaces():
    return render_template('home.html', cities=mongo.db.cities.find(), coworkingspaces=mongo.db.coworkingspaces.find())



@app.route('/show_results', methods=['POST'])
def show_results():
    
    city_name = request.form['city_name']  
    city_results = mongo.db.cities.find({"city_name": (city_name)})
 #  return redirect(url_for('get_coworkingspaces'))
    return render_template('home.html', cities=city_name, city=city_results)

    
  #  city = request.form['city']      
  #  filtered_city = mongo.db.cities.find({"region": (city)})

@app.route("/about")
def about():
    return render_template("about.html")
    
    
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
                          
    
@app.route('/update_coworkingspace/<coworkingspace_id>', methods=["POST"])
def update_coworkingspace(coworkingspace_id):
    coworkingspaces = mongo.db.coworkingspaces
    coworkingspaces.update( {'_id': ObjectId(coworkingspace_id)},
    {
        'city_name':request.form.get('city_name'),
        'coworking_name':request.form.get('coworking_name'),
        'coworking_description': request.form.get('coworking_description'),
        'coworking_address': request.form.get('coworking_address'),
        'opening_hours':request.form.get('opening_hours'),
        'website_url':request.form.get('website_url'),
        'img_url':request.form.get('img_url')
    })
    return redirect(url_for('get_coworkingspaces'))


@app.route("/delete_coworkingspace/<coworkingspace_id>")
def delete_coworkingspace(coworkingspace_id):
    mongo.db.coworkingspaces.remove({'_id': ObjectId(coworkingspace_id)})
    return redirect(url_for('get_coworkingspaces'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            